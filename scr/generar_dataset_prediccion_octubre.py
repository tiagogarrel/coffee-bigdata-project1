import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Cargar pronóstico de clima por cafetería
clima_df = pd.read_csv("pronostico_clima_octubre_por_cafeteria.csv", parse_dates=["fecha"])

# Conectar y traer cafeterías y productos únicos
engine = create_engine("postgresql://coffee:localpass123@localhost:5432/coffee_db")
ventas = pd.read_sql("SELECT DISTINCT cafeteria_id, producto FROM ventas", con=engine)

# Crear combinaciones: fecha x cafeteria x producto
fechas = pd.date_range(start="2024-10-01", end="2024-10-31", freq="D")
cafeterias = clima_df['cafeteria_id'].unique()
productos = ventas['producto'].unique()

combinaciones = pd.MultiIndex.from_product(
    [fechas, cafeterias, productos],
    names=["fecha", "cafeteria_id", "producto"]
).to_frame(index=False)

# Merge clima pronosticado
pred_df = combinaciones.merge(
    clima_df[['fecha', 'cafeteria_id', 'clima']],
    on=["fecha", "cafeteria_id"],
    how="left"
)

# Agregar columnas necesarias
pred_df['dia_semana'] = pred_df['fecha'].dt.day_name()
pred_df['es_finde'] = pred_df['dia_semana'].isin(['Saturday', 'Sunday']).astype(int)
pred_df['temperatura'] = 20.0  # constante por ahora

# Exportar
pred_df.to_csv("dataset_prediccion_octubre.csv", index=False)
print("✅ Dataset 'dataset_prediccion_octubre.csv' generado.")
