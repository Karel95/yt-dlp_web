FROM python:3.11-slim

WORKDIR /app

# Instala dependencias necesarias
RUN apt-get update && apt-get install -y ffmpeg curl && \
    pip install flask && \
    curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && \
    chmod +x /usr/local/bin/yt-dlp

# Copia el código de la app
COPY ./app /app

# Expone el puerto donde correrá Flask
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]
