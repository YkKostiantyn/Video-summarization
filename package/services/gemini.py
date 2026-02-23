from google import genai
from google.genai import types
import os

class GeminiService:
    def __init__(self, api_key: str, model_name: str = "gemini-flash-latest"):
        try:
            # Створюємо клієнта замість genai.configure
            self.client = genai.Client(api_key=api_key)
            self.model_name = model_name
            
            # Налаштування безпеки в новому форматі
            self.safety_settings = [
                types.SafetySetting(
                    category="HARM_CATEGORY_HATE_SPEECH",
                    threshold="BLOCK_NONE",
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_HARASSMENT",
                    threshold="BLOCK_NONE",
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    threshold="BLOCK_NONE",
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_DANGEROUS_CONTENT",
                    threshold="BLOCK_NONE",
                ),
            ]
            print(f"Gemini Service initialized with model: {model_name}")

        except Exception as e:
            print(f"Error initializing Gemini Service: {e}")
            self.client = None

    def generate_answer(self, rag_prompt: str) -> str:
        if not self.client:
            return "Error: Gemini client was not initialized."

        try:
            # Викликаємо генерацію через client.models
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=rag_prompt,
                config=types.GenerateContentConfig(
                    safety_settings=self.safety_settings
                )
            )
            
            if response.text:
                return response.text
            else:
                return "Error: Received an empty response from Gemini."

        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            # Перевірка на блокування через безпеку в новому форматі
            if "finish_reason" in str(e).lower() or "safety" in str(e).lower():
                return "Error: The response was blocked due to safety settings."
            return "Error: Could not get answer from Gemini."