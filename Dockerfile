# Usamos una imagen base oficial de Python
FROM python:3.11-slim

# Copia el script de instalación de dependencias del sistema
COPY system-dependencies.sh .

# Da permisos de ejecución al script y ejecuta el script
RUN chmod +x system-dependencies.sh && ./system-dependencies.sh

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalamos las dependencias listadas en el requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido de nuestro proyecto al contenedor
COPY . .

ENV PYTHONPATH=/app

ENV XDG_RUNTIME_DIR=/tmp

# Comando por defecto para ejecutar el juego
CMD ["python", "src/game.py"]
