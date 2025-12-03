from transformers import pipeline

class LocalT5:
    def __init__(self, model_path: str):
        print(f"Download {model_path}")
        self.summarizer = pipeline("summarization", model = model_path, tokenizer=model_path, device=-1)

    def generate_answer(self, rag_prompt: str) -> str:
        try:
            context_part = rag_prompt.split("Context:\n")[1].split("\n\nQuestion:")[0]
            query_part = rag_prompt.split("Question:")[1].split("\nAnswer:")[0].strip()
        except Exception:
            context_part = rag_prompt
            query_part = ""

        t5_prompt = f"summarize: {context_part} \n\n (Based on the text above, answer this question: {query_part})"
        
        try:
            result = self.summarizer(t5_prompt, max_length=100, min_length=10)
            return result[0]['summary_text']
        except Exception as e:
            print(f"Error calling Local T5: {e}")
            return "Error: Could not get answer from T5."