import pandas as pd
from sqlalchemy import create_engine
from sklearn.metrics import mean_absolute_error, r2_score
import lightgbm as lgb

# Conexión a PostgreSQL
engine = create_engine("postgresql://coffee:localpass123@localhost:5432/coffee_db")
df = pd.read_sql("SELECT * FROM ventas", con=engine).dropna()

# Preparar columnas
df['fecha'] = pd.to_datetime(df['fecha'])
df['dia_semana'] = df['fecha'].dt.day_name()
df['es_finde'] = df['dia_semana'].isin(['Saturday', 'Sunday']).astype(int)

# Agrupar
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

# Parámetros a probar
param_grid = [
    {'n_estimators': 250, 'learning_rate': 0.025, 'max_depth': 12, 'num_leaves': 64},
    {'n_estimators': 300, 'learning_rate': 0.03,  'max_depth': 14, 'num_leaves': 80},
    {'n_estimators': 350, 'learning_rate': 0.02,  'max_depth': 12, 'num_leaves': 96},
    {'n_estimators': 200, 'learning_rate': 0.035, 'max_depth': 10, 'num_leaves': 72},
    {'n_estimators': 300, 'learning_rate': 0.025, 'max_depth': 13, 'num_leaves': 64},
]


results = []

# Entrenar y evaluar cada combinación
for params in param_grid:
    model = lgb.LGBMRegressor(
        **params,
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
