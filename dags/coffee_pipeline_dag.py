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
    schedule=None,  
    catchup=False,
    description='Simula y carga ventas de café en PostgreSQL',
) as dag:

    tarea_simulacion = PythonOperator(
        task_id='simular_y_cargar_ventas',
        python_callable=run_sales_pipeline,
    )

    tarea_simulacion
