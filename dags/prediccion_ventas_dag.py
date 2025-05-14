from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from prediccion_pipeline import (
    generate_future_weather,
    build_prediction_dataset,
    predict_and_store
)
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
}

with DAG(
    dag_id='prediccion_ventas_dag',
    default_args=default_args,
    schedule='@weekly',
    catchup=False,
    description='Genera clima futuro, dataset de predicción y guarda predicciones en PostgreSQL',
) as dag:

    generar_clima = PythonOperator(
        task_id='generar_clima_futuro',
        python_callable=generate_future_weather,
    )

    crear_dataset = PythonOperator(
        task_id='crear_dataset_prediccion',
        python_callable=build_prediction_dataset,
    )

    predecir_y_guardar = PythonOperator(
        task_id='predecir_y_guardar_ventas',
        python_callable=predict_and_store,
    )

    generar_clima >> crear_dataset >> predecir_y_guardar