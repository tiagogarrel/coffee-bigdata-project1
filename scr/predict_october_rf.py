import pandas as pd
import joblib

# Cargar dataset de predicción
df = pd.read_csv("dataset_prediccion_octubre.csv", parse_dates=["fecha"])

# Guardar columnas originales para el output
output_cols = df[['fecha', 'cafeteria_id', 'producto', 'clima', 'dia_semana', 'es_finde']].copy()

# Codificar variables categóricas (one-hot encoding)
X = pd.get_dummies(df.drop(columns=["fecha"]), dtype=float)

# Cargar modelo entrenado de Random Forest
modelo = joblib.load("modelo_randomforest_final.joblib")

# Predecir
predicciones = modelo.predict(X)

# Agregar las predicciones al dataframe
output_cols['predicho'] = predicciones

# Exportar resultado
output_cols.to_csv("predicciones_rf_octubre.csv", index=False)
print("✅ Archivo 'predicciones_rf_octubre.csv' generado exitosamente.")
