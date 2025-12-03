import google.generativeai as genai
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold

class GeminiService:
    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash"):
        try:
            genai.configure(api_key=api_key)
            
            safety_settings = {
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            }

            self.model = genai.GenerativeModel(
                model_name,
                safety_settings=safety_settings
            )
            print(f"Gemini Service initialized with model: {model_name}")

        except Exception as e:
            print(f"Error initializing Gemini Service: {e}")
            self.model = None

    def generate_answer(self, rag_prompt: str) -> str:
        if not self.model:
            return "Error: Gemini model was not initialized."

        try:
            response = self.model.generate_content(rag_prompt)
            
            if response.parts:
                return response.text
            else:
                return "Error: Received an empty response from Gemini."

        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            if "safety" in str(e).lower():
                return "Error: The response was blocked due to safety settings."
            return "Error: Could not get answer from Gemini."