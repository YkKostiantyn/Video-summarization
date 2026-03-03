from transformers import pipeline
import re

class LocalBART:
    def __init__(self, model_path: str):
        print(f"Downloading/Loading {model_path} from Hugging Face...")
        self.summarizer = pipeline("summarization", model=model_path, tokenizer=model_path, device=-1)

    def generate_answer(self, rag_prompt: str) -> str:
        try:
            context_part = rag_prompt.split("Context:\n")[1].split("\n\nQuestion:")[0]
            query_part = rag_prompt.split("Question:")[1].split("\nAnswer:")[0].strip()
        except Exception:
            context_part = rag_prompt
            query_part = ""

        if query_part:
            bart_prompt = f"Context: {context_part}\n\nQuestion: {query_part}\n\nAnswer:"
        else:
            bart_prompt = context_part
        
        try:
            result = self.summarizer(
                bart_prompt, 
                max_length=128, 
                min_length=20, 
                clean_up_tokenization_spaces=True
            )
            
            raw_summary = result[0]['summary_text']
            
            clean_output = raw_summary.replace("Â", "").replace("\xa0", " ")
            clean_output = re.sub(r'\s+', ' ', clean_output).strip()
            
            return clean_output
            
        except Exception as e:
            print(f"Error calling Local BART: {e}")
            return "Error: Could not get answer from BART."