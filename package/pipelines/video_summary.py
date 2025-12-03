import os
from services.video_processor import downl_extract_audio
from services.transcriber import transcribe_audio
from services.rag_retriever import build_chunks_index
from utils.file_utils import remove_file

def run_video_processing_pipeline(youtube_URL: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.dirname(current_dir)
    upload_dir = os.path.join(package_dir, "uploads")
    file_path = os.path.join(upload_dir, "transcript.txt")

    faiss_index_path = os.path.join(upload_dir, "faiss_index.bin")
    chunks_json_path = os.path.join(upload_dir, "chunks.json")
    transcript_path = os.path.join(upload_dir, "transcript.txt")

    audio_path = None
    try:
        audio_path = downl_extract_audio(youtube_URL)
        transcript_text = transcribe_audio(audio_path, filename = os.path.basename(transcript_path))
        build_chunks_index(transcript_text, faiss_index_path, chunks_json_path)

        return faiss_index_path, chunks_json_path
    except Exception as e:
        print("Error while executing pipeline.")
        return None, None
    finally:
        remove_file(audio_path)
     