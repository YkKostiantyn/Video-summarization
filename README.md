# AI Video Summarization Tool

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![RAG](https://img.shields.io/badge/RAG-FAISS-green?style=for-the-badge)

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
git clone [https://github.com/YOUR-USERNAME/video-summarization.git](https://github.com/YOUR-USERNAME/video-summarization.git)
cd video-summarization
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
HF_TOKEN=your_hugging_face_token
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
