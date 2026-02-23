import os
import sys
from dotenv import load_dotenv
import streamlit as st

# Ensure the 'package' folder is importable when running from project root
PACKAGE_DIR = os.path.join(os.path.dirname(__file__), "package")
if PACKAGE_DIR not in sys.path:
    sys.path.insert(0, PACKAGE_DIR)

from package.pipelines.video_summary import run_video_processing_pipeline
from package.services.rag_retriever import rag_answer
from package.services.local_t5 import LocalT5
from package.services.gemini import GeminiService

load_dotenv()

st.set_page_config(page_title="Video Summarizer", layout="wide")

st.title("Video Summarization UI")

with st.sidebar:
    st.header("Settings")
    model_choice = st.selectbox("Preferred model (lazy init)", ["Auto (best available)", "Local T5", "Gemini"])
    t5_hf_id = st.text_input("Local T5 HF id/path", value=os.getenv("HF_ID", "YKostiantyn/t5-base-tuned-video-summarizer"))
    gemini_key = st.text_input("Gemini API key", value=os.getenv("GOOGLE_API_KEY", ""))

if "index_path" not in st.session_state:
    st.session_state.index_path = None
if "chunks_path" not in st.session_state:
    st.session_state.chunks_path = None
if "transcript" not in st.session_state:
    st.session_state.transcript = None
if "service" not in st.session_state:
    st.session_state.service = None

yt_url = st.text_input("YouTube video URL", help="Enter YouTube URL to process (eg. https://www.youtube.com/watch?v=...)")

col1, col2 = st.columns([1, 3])
with col1:
    if st.button("Process Video"):
        if not yt_url:
            st.warning("Please enter a YouTube URL first.")
        else:
            with st.spinner("Running pipeline: download -> transcribe -> index..."):
                index_path, chunks_path = run_video_processing_pipeline(yt_url)
                if index_path and chunks_path:
                    st.session_state.index_path = index_path
                    st.session_state.chunks_path = chunks_path
                    # try to load transcript if present
                    transcript_file = os.path.join(PACKAGE_DIR, "uploads", "transcript.txt")
                    if os.path.exists(transcript_file):
                        try:
                            with open(transcript_file, "r", encoding="utf-8") as f:
                                st.session_state.transcript = f.read()
                        except Exception:
                            st.session_state.transcript = None
                    st.success("Pipeline finished. You can now ask questions.")
                else:
                    st.error("Pipeline failed — check server logs.")

with col2:
    st.subheader("Transcript (preview)")
    if st.session_state.transcript:
        st.text_area("Transcript text", value=st.session_state.transcript[:5000], height=300)
    else:
        st.info("No transcript available yet. Run the pipeline first.")

st.markdown("---")

st.header("Ask a question about the video")
query = st.text_input("Your question")
if st.button("Ask"):
    if not st.session_state.index_path or not st.session_state.chunks_path:
        st.warning("No processed video found. Run `Process Video` first.")
    elif not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving context and generating answer..."):
            rag_prompt = rag_answer(query, st.session_state.index_path, st.session_state.chunks_path)

            # Initialize chosen service lazily
            service = None
            if model_choice == "Local T5" or (model_choice == "Auto (best available)" and not gemini_key):
                try:
                    service = LocalT5(model_path=t5_hf_id)
                    st.session_state.service = service
                except Exception as e:
                    st.error(f"Could not initialize Local T5: {e}")
                    service = None

            if model_choice == "Gemini" or (model_choice == "Auto (best available)" and gemini_key):
                if gemini_key:
                    try:
                        service = GeminiService(api_key=gemini_key)
                        st.session_state.service = service
                    except Exception as e:
                        st.error(f"Could not initialize Gemini service: {e}")
                else:
                    if not service:
                        st.warning("Gemini key not provided — please set in sidebar or .env")

            if not service and st.session_state.service:
                service = st.session_state.service

            if not service:
                st.error("No answer-generation service available.")
            else:
                try:
                    answer = service.generate_answer(rag_prompt)
                    st.subheader("Answer")
                    st.write(answer)
                except Exception as e:
                    st.error(f"Error generating answer: {e}")

st.markdown("---")
st.caption("This Streamlit app runs the existing pipeline and uses available models to answer questions.")
