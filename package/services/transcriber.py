import os
import whisper

def transcribe_audio(audio_path, language = "en", model_size = "base", filename = "transcript.txt"):
    model = whisper.load_model(model_size, device="cpu")

    result = model.transcribe(audio_path, language = language)

    return result["text"]
