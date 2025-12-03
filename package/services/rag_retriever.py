import faiss
import numpy as np
import os
import json
from utils.text_utils import split_into_chanks
from sentence_transformers import SentenceTransformer


embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    return np.array(embed_model.encode(text, convert_to_numpy=True), dtype="float32")

def build_chunks_index(text: str, index_path: str, chunks_path: str):
    chunks = split_into_chanks(text, 500, 0)

    embeddings_list = [get_embedding(c) for c in chunks]
    embeddings_np = np.array(embeddings_list).astype('float32')

    dim = len(embeddings_list[0])
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings_np)

    faiss.write_index(index, index_path)

    with open(chunks_path, "w", encoding = "utf-8") as f:
        json.dump(chunks, f)


def rag_answer(query: str, index_path: str, chunks_path: str, k: int = 3):
    if not os.path.exists(index_path) or not os.path.exists(chunks_path):
        return "Error: index or file with chanks not found."
    index = faiss.read_index(index_path)

    with open(chunks_path, "r", encoding = "utf-8") as f:
        chunks = json.load(f)

    q_emb = get_embedding(query)

    distances, indices = index.search(np.array([q_emb]).astype('float32'), k=k)
    context = "\n".join([chunks[i] for i in indices[0]])
    
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return prompt
