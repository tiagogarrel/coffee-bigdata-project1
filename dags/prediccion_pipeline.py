import pandas as pd
import numpy as np
import random
import logging
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import joblib
import os
from config import DB_URL, CITIES_INFO, PRODUCTOS, CLIMAS, CLIMA_WEIGHTS, DIAS_SEMANA

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# DB engine
engine = create_engine(DB_URL)

# 🔮 Step 1: Generate future weather
def generate_future_weather():
    fechas = pd.date_range(start='2024-11-01', end='2024-11-07')
    data = []

    for fecha in fechas:
        for ciudad in CITIES_INFO.keys():
            clima = random.choices(CLIMAS, weights=CLIMA_WEIGHTS)[0]
            if clima == 'calor extremo':
                temp = random.uniform(31, 40)
            elif clima == 'frío extremo':
                temp = random.uniform(5, 14)
            else:
                temp = random.uniform(15, 30)

            data.append({
                'fecha': fecha.date(),
                'ciudad': ciudad,
                'temperatura': round(temp, 2),
                'clima': clima,
                'dia_semana': fecha.strftime('%A')
            })

    df = pd.DataFrame(data)
    df.to_sql("clima_futuro", con=engine, if_exists="replace", index=False)
    logging.info("✅ Future weather generated and saved to DB.")

# 🧱 Step 2: Build prediction dataset
def build_prediction_dataset():
    clima_df = pd.read_sql("SELECT * FROM clima_futuro", con=engine)

    registros = []
    for _, row in clima_df.iterrows():
        for producto in PRODUCTOS:
            registros.append({
                'fecha': row['fecha'],
                'ciudad': row['ciudad'],
                'producto': producto,
                'temperatura': row['temperatura'],
                'clima': row['clima'],
                'dia_semana': row['dia_semana']
            })

    df = pd.DataFrame(registros)
    df.to_sql("dataset_prediccion", con=engine, if_exists="replace", index=False)
    logging.info("✅ Prediction dataset built and saved to DB.")

# 🤖 Step 3: Predict and store
def predict_and_store():
    df = pd.read_sql("SELECT * FROM dataset_prediccion", con=engine)

    # Load model
    modelo = joblib.load("/opt/airflow/dags/model_random_forest.joblib")

    # Encode features
    df_encoded = pd.get_dummies(df, columns=['ciudad', 'producto', 'clima', 'dia_semana'], drop_first=True)

    # Add missing columns if needed
    expected_cols = modelo.feature_names_in_
    for col in expected_cols:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[expected_cols]

    # Predict
    df['ventas_predichas'] = modelo.predict(df_encoded)

    # Save to DB
    df.to_sql("predicciones_futuras", con=engine, if_exists="replace", index=False)
    logging.info("✅ Predictions generated and saved to DB.")