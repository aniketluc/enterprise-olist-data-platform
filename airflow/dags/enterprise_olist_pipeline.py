from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "Aniket",
    "depends_on_past": False,
    "retries": 2,
}

with DAG(
    dag_id="enterprise_olist_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
    tags=["olist", "data-engineering"],
) as dag:

    start = EmptyOperator(
        task_id="start_pipeline"
    )

    upload_to_s3 = BashOperator(
    task_id="upload_raw_data_to_s3",
    bash_command="""
    cd /opt/airflow/project &&
    python ingestion/load/upload_to_s3.py
    """
    )

    bronze = EmptyOperator(
        task_id="bronze_ingestion"
    )

    silver = EmptyOperator(
        task_id="silver_transformation"
    )

    gold = EmptyOperator(
        task_id="gold_transformation"
    )

    snowflake = EmptyOperator(
        task_id="load_to_snowflake"
    )

    dbt = EmptyOperator(
        task_id="run_dbt_models"
    )

    end = EmptyOperator(
        task_id="pipeline_completed"
    )

    (
        start
        >> upload_to_s3
        >> bronze
        >> silver
        >> gold
        >> snowflake
        >> dbt
        >> end
    )