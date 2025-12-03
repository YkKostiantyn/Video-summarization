# AI Video Summarization Tool

<<<<<<< HEAD
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/GenAI-Gemini%20%2F%20T5-orange)
![RAG](https://img.shields.io/badge/RAG-FAISS-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)

Цей проєкт — інтелектуальна система для автоматичного створення коротких підсумків (summary) з відео.
Головна особливість — **гібридна архітектура**, яка дозволяє вибирати між потужністю хмарних моделей (**Google Gemini**) та приватністю локальних (**Fine-tuned T5**), використовуючи RAG для підвищення точності.

---

## 🚀 Основні можливості

* **🎙️ Розумна транскрибація:** Використання OpenAI Whisper для точного перетворення мови в текст.
* **🧠 RAG (Retrieval-Augmented Generation):** Система векторизує транскрипт (FAISS), щоб модель "бачила" контекст і давала точніші відповіді без галюцинацій.
* **🔄 Гібридний режим (Hybrid AI):**
    * **Cloud:** Використовує Google Gemini Pro для максимальної якості.
    * **Local:** Автоматичне перемикання на донавчену модель **T5**, якщо немає інтернету або потрібна приватність.
* **🛠️ Fine-tuning:** Включає Jupyter Notebooks для донавчання власних моделей на датасетах новин (CNN/DailyMail).
* **☁️ Hugging Face Integration:** Скрипти для автоматичного завантаження та версіонування моделей (`push_model.py`).

---

## 🛠 Технологічний стек

* **Core:** Python 3.10+
* **LLMs:** Google Generative AI (Gemini), T5 (Transformers)
* **Vector Store:** FAISS (Facebook AI Similarity Search)
* **Audio Processing:** FFmpeg, OpenAI Whisper
* **Data Science:** Pandas, Torch, Jupyter

---

## 📂 Структура проєкту

Проєкт побудований за принципами чистої архітектури:

```text
VIDEO-SUMMARIZATION/
├── model_training/      # Jupyter Notebooks для донавчання моделі T5
├── package/
│   ├── pipelines/       # Логіка оркестрації (основний потік даних)
│   ├── services/        # Бізнес-логіка (Gemini, T5, RAG, Video Processor)
│   ├── uploads/         # Тимчасове сховище для відео та векторних індексів
│   └── utils/           # Допоміжні утиліти (робота з текстом/файлами)
├── local_models/        # Збережені ваги локальних моделей
├── app.py               # Точка входу в програму
├── push_model.py        # Скрипт для деплою моделі на Hugging Face Hub
└── requirements.txt     # Залежності проєкту
=======
An intelligent system for automated video summarization.
This project features a **hybrid architecture** that combines the power of cloud LLMs with the privacy of local models, utilizing **RAG (Retrieval-Augmented Generation)** to ensure high accuracy and context awareness.

---

## Features

*  Smart Transcription: Utilizes **OpenAI Whisper** for high-precision speech-to-text conversion.
*  RAG (Retrieval-Augmented Generation): Implements **FAISS** for vector search. The model grounds its answers in specific video segments rather than hallucinating.
*  Hybrid Mode:
    * Cloud Mode: Leverages the **Google Gemini Pro** API for maximum detail and reasoning capabilities.
    * Local Mode: Uses a fine-tuned **T5** model that is automatically downloaded from the **Hugging Face Hub** and cached locally. This allows for **local inference** on your own hardware, ensuring data privacy without sending text to third parties.
*  MLOps Pipeline: Implements a full lifecycle: Data Collection -> Fine-tuning -> Push to HF Hub -> Automatic Client Deployment.

---

## Tech Stack

* Language: Python 3.10+
* LLM & AI: Google Generative AI (Gemini), Transformers (Hugging Face)
* Vector Store: FAISS (Facebook AI Similarity Search)
* Audio Processing: FFmpeg, OpenAI Whisper
* Tools: Pandas, Jupyter Notebooks

---

## Project Structure

The project follows a modular architecture for scalability:

```text
VIDEO-SUMMARIZATION/
├── model_training/      # Jupyter Notebooks for T5 Model Fine-tuning
├── package/
│   ├── pipelines/       # Orchestration logic (Video -> Text -> Summary)
│   ├── services/        # Core services: Gemini API, Local Model Loader, RAG Retriever
│   ├── uploads/         # Storage for input videos and FAISS indexes
│   └── utils/           # Helper functions (File I/O, Text processing)
├── app.py               # Entry point (CLI Application)
└── requirements.txt     # Project dependencies
```

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YkKostiantyn/Video-summarization.git
cd Video-summarization
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install System Dependencies
**FFmpeg** is required for audio extraction. Ensure it is installed and added to your PATH:
* **Windows:** `winget install ffmpeg` (or download from the official site)
* **Ubuntu/Debian:** `sudo apt install ffmpeg`
* **macOS:** `brew install ffmpeg`

### 4. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Configuration (.env)
Create a `.env` file in the root directory and add your API keys:
```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## Usage

### Run:

```bash
python app.py
```
And place your video link in the path when prompted.

The pipeline will perform the following:
1.  Extract audio from the video.
2.  Transcribe audio using Whisper.
3.  Build a vector index (FAISS).
4.  Generate a summary (using Gemini or the Local T5 model).

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
>>>>>>> b38b9dcaf3b603942aed3d44d73e190dcc11212a
