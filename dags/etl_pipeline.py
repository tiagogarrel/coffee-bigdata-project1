import pandas as pd
import random
import logging
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from config import DB_URL

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_sales_pipeline():
    # Crear engine desde config
    engine = create_engine(DB_URL)

    cities_info = {
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

    products = {
        'Flat White': 4.2,
        'Cappuccino': 4.5,
        'Latte': 5.0,
        'Mocha': 5.0,
        'Cold Brew': 5.5,
        'Espresso': 4.0
    }

    product_weights = {
        'default':      [30, 25, 20, 10, 10, 5],
        'calor_extremo': [20, 15, 15, 10, 35, 5],
        'frio_extremo':  [25, 20, 20, 25, 5, 5]
    }

    weather_conditions = [
        'soleado', 'parcialmente nublado', 'nublado',
        'lluvia', 'tormenta', 'viento fuerte',
        'calor extremo', 'frío extremo'
    ]
    weather_weights = [20, 15, 15, 10, 5, 10, 10, 15]

    def generar_clima():
        clima = random.choices(population=weather_conditions, weights=weather_weights, k=1)[0]
        if clima == 'calor extremo':
            temperatura = random.uniform(31, 40)
        elif clima == 'frío extremo':
            temperatura = random.uniform(5, 14)
        else:
            temperatura = random.uniform(15, 30)
        return clima, round(temperatura, 2)

    def generar_cafeterias():
        cafeterias = []
        for city, info in cities_info.items():
            for i in range(1, info['cafeterias'] + 1):
                lat = info['lat'] + random.uniform(-0.03, 0.03)
                lon = info['lon'] + random.uniform(-0.03, 0.03)
                cafeterias.append({
                    'cafeteria_id': f"{city[:3]}_c{i}",
                    'ciudad': city,
                    'lat': round(lat, 5),
                    'lon': round(lon, 5)
                })
        return pd.DataFrame(cafeterias)

    def simulate_day(date):
        cafeterias_df = generar_cafeterias()
        all_data = []
        for _, row in cafeterias_df.iterrows():
            clima, temp = generar_clima()
            base_tickets = random.randint(80, 130)
            if date.weekday() >= 5:
                base_tickets *= 1.3
            if clima in ['lluvia', 'tormenta', 'frío extremo']:
                base_tickets *= 0.75
            base_tickets = int(base_tickets)
            for t in range(base_tickets):
                n_items = random.choices([1, 2, 3, 4, 5], weights=[50, 25, 15, 7, 3])[0]
                hora = random.randint(6, 16)
                turno = 'mañana' if hora < 12 else 'tarde'
                ticket_id = f"{row['cafeteria_id']}_{date:%Y%m%d}_{hora}_{t}"
                clima_key = 'default'
                if clima == 'calor extremo':
                    clima_key = 'calor_extremo'
                elif clima == 'frío extremo':
                    clima_key = 'frio_extremo'
                for _ in range(n_items):
                    producto = random.choices(list(products.keys()), weights=product_weights[clima_key], k=1)[0]
                    precio = products[producto]
                    cantidad = random.randint(1, 3)
                    monto_total = round(precio * cantidad, 2)
                    all_data.append({
                        'ticket_id': ticket_id,
                        'fecha': date.date(),
                        'ciudad': row['ciudad'],
                        'cafeteria_id': row['cafeteria_id'],
                        'producto': producto,
                        'precio_unitario': precio,
                        'cantidad': cantidad,
                        'monto_total': monto_total,
                        'hora': hora,
                        'turno': turno,
                        'dia_semana': date.strftime('%A'),
                        'temperatura': temp,
                        'clima': clima,
                        'lat': row['lat'],
                        'lon': row['lon']
                    })
        return pd.DataFrame(all_data)

    # Loop principal
    start_date = datetime(2024, 5, 1)
    end_date = datetime(2024, 10, 31)
    current_date = start_date
    while current_date <= end_date:
        logging.info(f"📅 Simulating: {current_date.date()}")
        df_day = simulate_day(current_date)
        df_day.to_sql("ventas", con=engine, if_exists="append", index=False)
        current_date += timedelta(days=1)

    logging.info("✅ Simulation completed and data loaded into PostgreSQL.")