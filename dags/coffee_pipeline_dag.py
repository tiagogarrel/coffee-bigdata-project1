from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl_pipeline import run_sales_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
}

with DAG(
    dag_id='ventas_cafe_dag',
    default_args=default_args,
    schedule_interval=None,  # No automatic schedule
    catchup=False,
    description='Simulates and loads coffee sales into PostgreSQL',
) as dag:

    simulate_and_load_sales = PythonOperator(
        task_id='simulate_and_load_sales',
        python_callable=run_sales_pipeline,
    )

    simulate_and_load_sales
