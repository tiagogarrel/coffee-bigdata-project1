import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Conexión a PostgreSQL
engine = create_engine("postgresql://coffee:localpass123@localhost:5432/coffee_db")
df = pd.read_sql("SELECT * FROM ventas", con=engine).dropna()

# Preparación de datos
df['fecha'] = pd.to_datetime(df['fecha'])
df['dia_semana'] = df['fecha'].dt.day_name()
df['es_finde'] = df['dia_semana'].isin(['Saturday', 'Sunday']).astype(int)

# Agregación
agg_df = df.groupby(['fecha', 'cafeteria_id', 'producto', 'clima', 'dia_semana', 'es_finde'], as_index=False).agg({
    'cantidad': 'sum',
    'temperatura': 'mean'
})

# División temporal
train_df = agg_df[agg_df['fecha'] < '2024-10-01']
test_df = agg_df[agg_df['fecha'] >= '2024-10-01']

# Target y features
y_train = train_df['cantidad'].astype(float)
X_train = train_df.drop(columns=['cantidad'])
X_train_encoded = pd.get_dummies(X_train.drop(columns=['fecha']), dtype=float)

y_test = test_df['cantidad'].astype(float)
X_test = test_df.drop(columns=['cantidad'])
X_test_encoded = pd.get_dummies(X_test.drop(columns=['fecha']), dtype=float)

# Reindex test para que tenga mismas columnas
X_test_encoded = X_test_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)

# Entrenar modelo
modelo = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)


modelo.fit(X_train_encoded, y_train)

# Predicción
y_pred = modelo.predict(X_test_encoded)

# Resultados detallados
resultados = X_test[['fecha', 'cafeteria_id', 'producto', 'clima', 'dia_semana', 'es_finde']].copy()
resultados['real'] = y_test.values
resultados['predicho'] = y_pred
resultados['error'] = resultados['real'] - resultados['predicho']

# Exportar CSV
resultados.to_csv("resultados_randomforest_temporal.csv", index=False)

# Métricas
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ CSV 'resultados_randomforest_temporal.csv' generado.")
print(f"✅ MAE: {mae:.2f}")
print(f"✅ R² Score: {r2:.3f}")

import joblib

# Guardar el modelo entrenado
joblib.dump(modelo, "modelo_randomforest_final.joblib")
print("✅ Modelo guardado como 'modelo_randomforest_final.joblib'")

