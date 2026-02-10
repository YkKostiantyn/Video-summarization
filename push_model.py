from huggingface_hub import HfApi
import os

# Введіть своє ім'я користувача на Hugging Face
HF_USERNAME = "YKostiantyn" 

# Ім'я репозиторію на Hugging Face Hub
REPO_NAME = "t5-base-tuned-video-summarizer"
REPO_ID = f"{HF_USERNAME}/{REPO_NAME}"

# Шлях до вашої локальної папки моделі (використовуйте точний шлях, як на скріншоті)
# Цей шлях відносний до місця запуску скрипта
LOCAL_MODEL_DIR = "local_models/t5_base_summarizer"

# Повідомлення для коміту (історія версій)
COMMIT_MSG = "Initial upload of fine-tuned T5 base summarizer model"

print(f"--- Підготовка до завантаження моделі: {REPO_ID} ---")

# --- 1. Перевірка автентифікації ---
try:
    api = HfApi()
    # Перевіряємо, чи ви авторизовані через 'huggingface-cli login'
    print(f"✅ Успішно авторизовано як: {api.whoami()['name']}")
except Exception as e:
    print("❌ Помилка автентифікації. Будь ласка, запустіть 'huggingface-cli login' у терміналі.")
    exit()

# --- 2. Перевірка локальної папки ---
if not os.path.exists(LOCAL_MODEL_DIR):
    print(f"❌ Помилка: Локальна директорія '{LOCAL_MODEL_DIR}' не знайдена.")
    print("Перевірте, чи правильно вказано шлях.")
    exit()

# --- 3. Створення/Перевірка репозиторію ---
print(f"🌀 Створення/Перевірка репозиторію: {REPO_ID}")
api.create_repo(
    repo_id=REPO_ID,
    exist_ok=True, # Не викликатиме помилки, якщо репозиторій вже існує
    repo_type="model"
)

print(f"⬆️ Завантаження вмісту з {LOCAL_MODEL_DIR}...")
api.upload_folder(
    folder_path=LOCAL_MODEL_DIR,
    repo_id=REPO_ID,
    commit_message=COMMIT_MSG,
    # Можна додати ignore_patterns=['*.bin', '*.py'] для виключення певних файлів
)

print("-" * 40)
print(f"🎉 Успішно завантажено модель на: https://huggingface.co/{REPO_ID}")
print("Тепер ви можете завантажити її у своєму проєкті, використовуючи цей ID.")