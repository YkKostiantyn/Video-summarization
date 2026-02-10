# Використовуємо Python 3.11 (slim версія легша)
FROM python:3.11-slim

# 1. Встановлюємо системні залежності
# Твоєму скрипту потрібен FFmpeg для роботи з аудіо/відео!
# git потрібен для деяких бібліотек пітону
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# 2. Робоча папка
WORKDIR /app

# 3. Копіюємо файл залежностей
COPY requirements.txt .

# 4. Встановлюємо бібліотеки
# --no-cache-dir зменшує розмір образу
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копіюємо весь код проєкту
COPY . .

# 6. Команда запуску
# python -u вмикає небуферизований вивід (щоб print() з'являвся одразу)
CMD ["python", "-u", "package/app.py"]