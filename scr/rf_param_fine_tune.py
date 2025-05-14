import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Conexión a PostgreSQL
engine = create_engine("postgresql://coffee:localpass123@localhost:5432/coffee_db")
df = pd.read_sql("SELECT * FROM ventas", con=engine).dropna()

# Procesamiento
df['fecha'] = pd.to_datetime(df['fecha'])
df['dia_semana'] = df['fecha'].dt.day_name()
df['es_finde'] = df['dia_semana'].isin(['Saturday', 'Sunday']).astype(int)

# Agregar por día
agg_df = df.groupby(['fecha', 'cafeteria_id', 'producto', 'clima', 'dia_semana', 'es_finde'], as_index=False).agg({
    'cantidad': 'sum',
    'temperatura': 'mean'
})

# Split temporal
train_df = agg_df[agg_df['fecha'] < '2024-10-01']
test_df = agg_df[agg_df['fecha'] >= '2024-10-01']

# Features y target
y_train = train_df['cantidad'].astype(float)
X_train = train_df.drop(columns=['cantidad', 'fecha'])
X_train = pd.get_dummies(X_train, columns=['cafeteria_id', 'producto', 'clima', 'dia_semana']).astype(float)

y_test = test_df['cantidad'].astype(float)
X_test = test_df.drop(columns=['cantidad', 'fecha'])
X_test = pd.get_dummies(X_test, columns=['cafeteria_id', 'producto', 'clima', 'dia_semana']).astype(float)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# Hiperparámetros a probar
param_grid = [
    {'n_estimators': 200, 'max_depth': 12, 'min_samples_split': 4},
    {'n_estimators': 250, 'max_depth': 14, 'min_samples_split': 3},
    {'n_estimators': 300, 'max_depth': 10, 'min_samples_split': 5},
    {'n_estimators': 200, 'max_depth': 10, 'min_samples_split': 2},
]
# Entrenar y evaluar
results = []
for params in param_grid:
    model = RandomForestRegressor(
        n_estimators=params['n_estimators'],
        max_depth=params['max_depth'],
        min_samples_split=params['min_samples_split'],
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results.append({
        **params,
        'MAE': round(mae, 2),
        'R2': round(r2, 3)
    })

# Mostrar resultados
results_df = pd.DataFrame(results)
print(results_df)

results_df.to_csv("temporal.csv", index=False)
