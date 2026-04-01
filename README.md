# AI Video Summarization Tool 

An intelligent system for automated video summarization. This project features a **hybrid architecture** that combines the power of cloud LLMs with the privacy of local models, utilizing **RAG (Retrieval-Augmented Generation)** to ensure high accuracy and context awareness.

##  Features

- **Smart Transcription:** Utilizes **OpenAI Whisper** for high-precision speech-to-text conversion.
- **RAG (Retrieval-Augmented Generation):** Implements **FAISS** for vector search. The model grounds its answers in specific video segments rather than hallucinating.
- **Hybrid Mode:**
  - **Cloud Mode:** Leverages the **Google Gemini Pro** API for maximum detail and reasoning capabilities.
  - **Local Mode:** Uses a fine-tuned **T5** model that is automatically downloaded from the **Hugging Face Hub** and cached locally. This allows for **local inference** on your own hardware, ensuring data privacy without sending text to third parties.
- **Dockerized:** Fully containerized application with pre-configured environments (Python, FFmpeg, Drivers).
- **MLOps Pipeline:** Implements a full lifecycle: Data Collection -> Fine-tuning -> Push to HF Hub -> Automatic Client Deployment.

##  Tech Stack

- **Containerization:** Docker, Docker Compose
- **Language:** Python 3.11
- **LLM & AI:** Google Generative AI (Gemini), Transformers (Hugging Face)
- **Vector Store:** FAISS (Facebook AI Similarity Search)
- **Audio Processing:** FFmpeg, OpenAI Whisper
- **Tools:** Pandas, Jupyter Notebooks

##  Project Structure

    VIDEO-SUMMARIZATION/
    ├── model_training/      # Jupyter Notebooks for T5 Model Fine-tuning
    ├── package/
    │   ├── pipelines/       # Orchestration logic (Video -> Text -> Summary)
    │   ├── services/        # Core services: Gemini API, Local Model Loader, RAG Retriever
    │   ├── uploads/         # Storage for input videos and FAISS indexes (Persisted via Docker Volume)
    │   └── utils/           # Helper functions (File I/O, Text processing)
    ├── app.py               # Entry point (CLI Application)
    ├── Dockerfile           # Docker image configuration
    ├── docker-compose.yml   # Container orchestration
    └── requirements.txt     # Project dependencies

##  Installation & Setup

You don't need to install Python, FFmpeg, or any libraries manually. The only requirement is Docker.

### 1. Install Docker

Before starting, ensure you have Docker installed and **running**:

* **Windows / macOS:** Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
* **Linux (Ubuntu/Debian):**

        sudo apt-get update
        sudo apt-get install docker.io docker-compose

### 2. Clone the Repository

    git clone [https://github.com/YkKostiantyn/Video-summarization.git](https://github.com/YkKostiantyn/Video-summarization.git)
    cd Video-summarization

### 3. Environment Configuration

Create a `.env` file in the root directory. This is required for the Gemini API.

    # Create a file named .env and add your key:
    GOOGLE_API_KEY=your_gemini_api_key_here

### 4. Run the Application

Open your terminal in the project folder and run:

    docker-compose up --build

*Note: The first launch may take a few minutes as it downloads the base image (approx. 1-2GB) and AI models.*

##  Usage

Once the container starts, you will see an interactive menu in your terminal:

1.  **Select the Model:** Choose between **1: Local T5** (Privacy focused) or **2: Gemini** (Cloud power).
2.  **Provide Video URL:** Paste a YouTube link when prompted.
3.  **Ask Questions:** Interact with the video content via chat.

**Note:** All downloaded videos, transcripts, and FAISS indexes are saved in the `package/uploads/` folder on your local machine, so you can access them even after stopping Docker.

To stop the application, press `Ctrl+C` in the terminal.

##  License

Distributed under the MIT License. See `LICENSE` for more information.
