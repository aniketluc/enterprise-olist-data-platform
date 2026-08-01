from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def greet():
    print("Welcome to the Enterprise Olist Data Platform!")
    
with DAG(
    'hello_world',
    schedule_interval=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:
    
    greet_task = PythonOperator(
        task_id='print_message',
        python_callable=greet
    )
    
    greet_task