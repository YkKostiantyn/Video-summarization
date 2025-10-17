import os

def split_into_chanks(text: str, chunk_size: str = 500, overlap = 0):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

def save_text(data, destination: str, filename: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.dirname(current_dir)
    out_dir = os.path.join(package_dir, destination)

    out_text = os.path.join(out_dir, filename)

    with open(out_text, "w", encoding="utf-8") as f:
        f.write(data)