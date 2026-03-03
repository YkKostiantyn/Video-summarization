import os
from dotenv import load_dotenv
from pipelines.video_summary import run_video_processing_pipeline
from services.rag_retriever import rag_answer
from services.gemini import GeminiService
# 1. Змінили імпорт з LocalT5 на LocalBART
from services.local_bart import LocalBART 

def main():
    load_dotenv()

    # 2. Вказали репозиторій твоєї свіжої моделі BART
    HF_ID = "YKostiantyn/fine-tuned-bart-model-summarizer"
    bart_service = None
    
    try:
        # 3. Ініціалізуємо сервіс BART
        bart_service = LocalBART(model_path=HF_ID)
        print(f"BART Service initialized from Hub: {HF_ID}")
    except Exception as e:
        print(f"Error initializing BART from Hub ({e}).")

    gemini_key = os.getenv("GOOGLE_API_KEY")
    gemini_service = None
    if not gemini_key:
        print("GOOGLE_API_KEY not found in .env.")
    else:
        gemini_service = GeminiService(api_key=gemini_key)

    if not bart_service and not gemini_service:
        print("No models are available.")
        return

    print("-" * 30)

    chosen_service = None
    while chosen_service is None:
        print("Which model do you want to use for answers?")
        if bart_service:
            print("1: Local BART") # Оновили текст меню
        if gemini_service:
            print("2: Gemini")
        
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == "1" and bart_service:
            chosen_service = bart_service
            print("Using BART for answers.")
        elif choice == "2" and gemini_service:
            chosen_service = gemini_service
            print("Using Gemini for answers.")
        else:
            print("Invalid choice, please try again.")
    
    print("-" * 30)

    youtube_URL = input("Enter video URL: ")

    index_path, chunks_path = run_video_processing_pipeline(youtube_URL)

    if index_path and chunks_path and os.path.exists(chunks_path):
        while True:
            query = input("Ask anything (type 'exit' to quit): ")
            if query.lower() in ["exit"]:
                break
            rag_prompt = rag_answer(query, index_path, chunks_path)
            
            print(f"Generating answer using {chosen_service.__class__.__name__}...")
            final_answer = chosen_service.generate_answer(rag_prompt)
            
            print(f"\nAnswer: {final_answer}")
            print("-" * 30)
    else:
        print("Couldn't create index.")

if __name__ == "__main__":
    main()