import logging

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

from config import DB_URL

# Configure logging format
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load data from the database
engine = create_engine(DB_URL)
df = pd.read_sql("SELECT * FROM predicciones_futuras", con=engine)

# Plot 1: Predicted sales by product
plt.figure(figsize=(10, 6))
df.groupby("producto")["ventas_predichas"].sum().sort_values().plot(kind="barh")
plt.title("Predicted sales by product")
plt.xlabel("Estimated units")
plt.tight_layout()
plt.savefig("reports/ventas_por_producto.png")
plt.close()
logging.info("📊 Saved: ventas_por_producto.png")

# Plot 2: Predicted sales by city
plt.figure(figsize=(10, 6))
df.groupby("ciudad")["ventas_predichas"].sum().sort_values().plot(kind="barh", color="teal")
plt.title("Predicted sales by city")
plt.xlabel("Estimated units")
plt.tight_layout()
plt.savefig("reports/ventas_por_ciudad.png")
plt.close()
logging.info("📊 Saved: ventas_por_ciudad.png")

# Plot 3: Boxplot of predictions by weather
plt.figure(figsize=(10, 6))
df.boxplot(column="ventas_predichas", by="clima", rot=45)
plt.title("Prediction distribution by weather type")
plt.suptitle("")
plt.ylabel("Predicted sales")
plt.tight_layout()
plt.savefig("reports/boxplot_por_clima.png")
plt.close()
logging.info("📊 Saved: boxplot_por_clima.png")

logging.info("✅ All visualizations exported to /reports")
