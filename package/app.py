import os
from pipelines.video_summary import run_video_processing_pipeline
from services.rag_retriever import rag_answer

if __name__ == "__main__":
    youtube_URL = input("Enter video URL:")
    index_path, chunks_path = run_video_processing_pipeline(youtube_URL)

    if index_path and chunks_path and os.path.exists(chunks_path):
        while True:
            query = input("Ask anything: ")
            if query.lower() in ["exit"]:
                break
            answer = rag_answer(query, index_path, chunks_path)
            print(f"\nQuery: {query}\nAnswer: {answer}")
    else:
        print("Coulnt create index. ")
