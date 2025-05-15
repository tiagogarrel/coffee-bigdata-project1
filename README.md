# ☕ Coffee Big Data Project

This project simulates, stores, visualizes, and predicts coffee shop sales across various Australian cities. It combines data simulation, processing, machine learning, visualization with Power BI, and orchestration with Apache Airflow to showcase a complete and realistic end-to-end data pipeline.

---

## 🚀 Project Components

### 🔄 Sales Simulation
- Daily simulation of sales tickets per city, coffee shop, and product.
- Takes into account weather, weekends, temperature, and product popularity.
- Artificially generated dataset with over 1.3 million rows.

### 🗃️ Data Storage
- PostgreSQL database managed through Docker.
- Automated data loading using `SQLAlchemy`.

### 📊 Visualization
- Power BI dashboard connected directly to the PostgreSQL database.
- Additional visualizations using Matplotlib (sales by product, city, and weather).

### 🤖 Predictive Modeling
- Trained models (Random Forest and LightGBM).
- Forecasting using "future" weather data with varying accuracy levels.
- Predictions exported back to PostgreSQL.

### ⛅ Automated Forecasting
- Future weather generation for target prediction dates.
- Structured prediction dataset creation.
- Daily sales predictions per product and coffee shop.

### ⚙️ Orchestration with Apache Airflow
- Complete pipeline automated via DAGs.
- Individual DAGs for simulation, loading, prediction, and export.

---

## 🧱 Project Structure

```
coffee-bigdata-project/
├── dags/
│   ├── coffee_pipeline_dag.py
│   ├── prediccion_ventas_dag.py
│   ├── run_pipeline.py
│   ├── prediccion_pipeline.py
│   ├── model_random_forest.joblib
│   ├── config.py
│   └── visualize_predictions.py
├── airflow/
│   ├── .env
│   ├── config/
│   ├── logs/
│   └── plugins/
├── models/
│   └── model_lightgbm.joblib
├── reports/
│   └── [matplotlib-generated visualizations]
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

---

## 📦 Tech Stack

- **Python** (Pandas, Scikit-learn, SQLAlchemy, Matplotlib, Dotenv)
- **PostgreSQL** (via Docker)
- **Power BI** (dashboard)
- **Apache Airflow** (CeleryExecutor orchestration)
- **Docker** (for all services)

---

## 🧪 Run Locally

1. Clone the repo:

```bash
git clone https://github.com/youruser/coffee-bigdata-project.git
cd coffee-bigdata-project
```

2. Create a `.env` file with your DB credentials:

```env
DB_USER=coffee
DB_PASS=localpass123
DB_HOST=db
DB_PORT=5432
DB_NAME=coffee_db
```

3. Start the services:

```bash
docker-compose up -d
```

4. Access Airflow UI: [http://localhost:8080](http://localhost:8080)  
   Username: `airflow` / Password: `airflow`

---

## 📈 Example Visuals

![Sales by Product](reports/ventas_por_producto.png)
![Boxplot by Weather](reports/boxplot_por_clima.png)

---

## ✨ Future Improvements

- Deploy interactive web dashboard (Node.js or Streamlit).
- Build a REST API for real-time forecasting.
- Incorporate special events, promotions, and holidays into the simulation.
- Explore additional models: XGBoost, CatBoost, Prophet.

---

## 👨‍💻 Author

**Tiago Garrel** – Production Engineer & Data Analyst  
[LinkedIn](https://www.linkedin.com/in/tiago-garrel-329031209/)