# Utiliza una imagen base de Python adecuada para tu proyecto Django
FROM python:3.9

# Establece el directorio de trabajo en la raíz de la aplicación
WORKDIR /app

# Copia los archivos de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el código fuente de la aplicación al contenedor
COPY . .

# Expone el puerto 8000 para acceder a la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
