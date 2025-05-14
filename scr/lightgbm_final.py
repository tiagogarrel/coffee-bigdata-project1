import pandas as pd
from sqlalchemy import create_engine
from sklearn.metrics import mean_absolute_error, r2_score
import lightgbm as lgb

# Conexión a PostgreSQL
engine = create_engine("postgresql://coffee:localpass123@localhost:5432/coffee_db")
df = pd.read_sql("SELECT * FROM ventas", con=engine).dropna()

# Preparación
df['fecha'] = pd.to_datetime(df['fecha'])
df['dia_semana'] = df['fecha'].dt.day_name()
df['es_finde'] = df['dia_semana'].isin(['Saturday', 'Sunday']).astype(int)

# Agregación diaria
agg_df = df.groupby(['fecha', 'cafeteria_id', 'producto', 'clima', 'dia_semana', 'es_finde'], as_index=False).agg({
    'cantidad': 'sum',
    'temperatura': 'mean'
})

# División temporal
train_df = agg_df[agg_df['fecha'] < '2024-10-01']
test_df = agg_df[agg_df['fecha'] >= '2024-10-01']

# Variables
y_train = train_df['cantidad'].astype(float)
X_train = pd.get_dummies(train_df.drop(columns=['cantidad', 'fecha']), dtype=float)

y_test = test_df['cantidad'].astype(float)
X_test = pd.get_dummies(test_df.drop(columns=['cantidad', 'fecha']), dtype=float)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# Entrenamiento con la mejor combinación
modelo = lgb.LGBMRegressor(
    n_estimators=250,
    learning_rate=0.025,
    max_depth=12,
    num_leaves=64,
    random_state=42,
    n_jobs=-1
)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# Resultados detallados
resultados = test_df[['fecha', 'cafeteria_id', 'producto', 'clima', 'dia_semana', 'es_finde']].copy()
resultados['real'] = y_test.values
resultados['predicho'] = y_pred
resultados['error'] = resultados['real'] - resultados['predicho']

# Exportar CSV
resultados.to_csv("resultados_lightgbm_temporal.csv", index=False)

# Métricas
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ CSV 'resultados_lightgbm_temporal.csv' generado.")
print(f"✅ MAE: {mae:.2f}")
print(f"✅ R² Score: {r2:.3f}")


import joblib

# Guardar el modelo entrenado
joblib.dump(modelo, "modelo_lightgbm_final.joblib")
print("✅ Modelo guardado como 'modelo_lightgbm_final.joblib'")
