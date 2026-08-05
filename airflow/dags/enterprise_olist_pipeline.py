from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

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

    bronze = BashOperator(
        task_id="bronze_ingestion",
        bash_command="""
        cd /opt/airflow/project &&
        python -m src.bronze.bronze_ingestion
        """
    )

    silver = BashOperator(
        task_id="silver_transformation",
        bash_command="""
        cd /opt/airflow/project &&
        python -m src.silver.silver_pipeline
        """
    )

    gold = BashOperator(
        task_id="gold_transformation",
        bash_command="""
        cd /opt/airflow/project &&
        python -m src.gold.run_gold
        """
    )

    snowflake = BashOperator(
        task_id="load_to_snowflake",
        bash_command="""
        cd /opt/airflow/project &&
        python -m src.snowflake_loader.load_gold_to_snowflake
        """
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
        cd /opt/airflow/project/olist_dbt &&
        dbt run
        """
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        cd /opt/airflow/project/olist_dbt &&
        dbt test
        """
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
        >> dbt_run
        >> dbt_test
        >> end
    )