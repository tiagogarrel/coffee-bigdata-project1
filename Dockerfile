# Imagen base con Python
FROM python:3.11-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY requirements.txt ./
COPY scr/ ./scr/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto: ejecutar el pipeline
CMD ["python", "scr/etl_pipeline.py"]
