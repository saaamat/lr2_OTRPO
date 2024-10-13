# Используем официальный образ Python
FROM python:3.12

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    && pip install opencv-python \
    && rm -rf /var/lib/apt/lists/*

# Копируем код в контейнер
WORKDIR /app
COPY . .

# Запускаем скрипт
CMD ["python", "main.py", "src/faces.jpg"]