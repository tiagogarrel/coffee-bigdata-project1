import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path



# Configuración de conexión a la base de datos (de acuerdo a docker-compose.yml)
DB_USER = 'coffee'
DB_PASS = 'coffee123'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'coffee_db'


# Ruta del archivo CSV
BASE_DIR = Path(__file__).resolve().parent.parent  # va dos niveles arriba (a la raíz del proyecto)
csv_path = BASE_DIR / 'data' / 'raw' / 'simulated_sales.csv'

print(csv_path)
#csv_path = r'C:\Users\user\OneDrive\Desktop\coffee-bigdata-project\data\raw\simulated_sales.csv'

# Leer el CSV simulado
df = pd.read_csv(csv_path)

# Crear el motor de conexión con SQLAlchemy
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Subir el dataframe a PostgreSQL como tabla 'ventas'
df.to_sql('ventas', con=engine, if_exists='replace', index=False)

print("✅ Datos cargados exitosamente en la tabla 'ventas'")
