import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Conexión a la base
engine = create_engine("postgresql://coffee:localpass123@localhost:5432/coffee_db")
df = pd.read_sql("SELECT * FROM ventas", con=engine)
df['fecha'] = pd.to_datetime(df['fecha'])

# Obtener clima real por fecha y cafetería
agg_df = df.groupby(['fecha', 'cafeteria_id'], as_index=False).agg({
    'clima': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan
})

# Filtrar sólo Octubre
oct_df = agg_df[(agg_df['fecha'] >= '2024-10-01') & (agg_df['fecha'] <= '2024-10-31')].copy()

# Lista de climas posibles
climas_posibles = df['clima'].dropna().unique().tolist()

# Función para simular error
def aplicar_ruido(clima, prob_error):
    if np.random.rand() < prob_error:
        return np.random.choice([c for c in climas_posibles if c != clima])
    return clima

# Función para nivel de precisión según la fecha
def get_prob_error(fecha):
    if fecha <= pd.Timestamp('2024-10-07'):
        return 0.05  # 95% precisión
    elif fecha <= pd.Timestamp('2024-10-14'):
        return 0.20
    else:
        return 0.50

# Aplicar clima pronosticado con ruido
oct_df['clima_pronosticado'] = oct_df.apply(
    lambda row: aplicar_ruido(row['clima'], get_prob_error(row['fecha'])),
    axis=1
)

# Guardar CSV
oct_df.to_csv("pronostico_clima_octubre_por_cafeteria.csv", index=False)
print("✅ Archivo 'pronostico_clima_octubre_por_cafeteria.csv' generado.")
