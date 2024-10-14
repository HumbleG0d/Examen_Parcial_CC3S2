# Usamos una imagen base oficial de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalamos las dependencias listadas en el requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido de nuestro proyecto al contenedor
COPY . .

# Ejecutamos los tests (BDD y unitarios) al construir la imagen, opcional
# RUN pytest && behave

# Comando por defecto para ejecutar el juego
CMD ["python", "game.py"]
