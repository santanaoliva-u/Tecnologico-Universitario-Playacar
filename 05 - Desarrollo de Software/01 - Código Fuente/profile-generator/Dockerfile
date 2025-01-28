# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos y la aplicación
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY . .

# Expone el puerto (si tu aplicación usa uno, si no puedes omitirlo)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
