import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables de entorno desde .env
load_dotenv()

# Parámetros de base de datos
DB_USER = os.getenv('DB_USER', 'coffee')
DB_PASS = os.getenv('DB_PASS', 'localpass123')
DB_HOST = os.getenv('DB_HOST', 'db') #or localhost
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'coffee_db')

# URL completa para SQLAlchemy
DB_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Rango de fechas de simulación
SIM_START_DATE = datetime(2024, 5, 1)
SIM_END_DATE = datetime(2024, 10, 31)

# Fechas de predicción
PRED_START_DATE = datetime(2024, 11, 1)
PRED_END_DATE = datetime(2024, 11, 7)

# Lista de productos
PRODUCTOS = ['Flat White', 'Cappuccino', 'Latte', 'Mocha', 'Cold Brew', 'Espresso']

# Lista de climas posibles
CLIMAS = ['soleado', 'parcialmente nublado', 'nublado', 'lluvia', 'tormenta', 'viento fuerte', 'calor extremo', 'frío extremo']

# Peso de cada clima (para simulación)
CLIMA_WEIGHTS = [20, 15, 15, 10, 5, 10, 10, 15]

# Días de la semana
DIAS_SEMANA = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Info por ciudad
CITIES_INFO = {
    'Sydney':     {'lat': -33.8688, 'lon': 151.2093, 'cafeterias': 15},
    'Melbourne':  {'lat': -37.8136, 'lon': 144.9631, 'cafeterias': 15},
    'Brisbane':   {'lat': -27.4698, 'lon': 153.0251, 'cafeterias': 10},
    'Perth':      {'lat': -31.9505, 'lon': 115.8605, 'cafeterias': 10},
    'Gold Coast': {'lat': -28.0167, 'lon': 153.4000, 'cafeterias': 6},
    'Cairns':     {'lat': -16.9186, 'lon': 145.7781, 'cafeterias': 6},
    'Adelaide':   {'lat': -34.9285, 'lon': 138.6007, 'cafeterias': 4},
    'Hobart':     {'lat': -42.8821, 'lon': 147.3272, 'cafeterias': 4},
    'Darwin':     {'lat': -12.4634, 'lon': 130.8456, 'cafeterias': 3},
    'Canberra':   {'lat': -35.2809, 'lon': 149.1300, 'cafeterias': 3}
}
