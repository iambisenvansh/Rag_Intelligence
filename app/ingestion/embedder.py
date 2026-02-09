import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(text_chunks: list[str]) -> np.ndarray:
    if not text_chunks:
        raise ValueError("No text chunks provided for embedding")

    embeddings = model.encode(
        text_chunks,
        show_progress_bar=False,
        convert_to_numpy=True
    )

    # Ensure correct shape for FAISS
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    return embeddings.astype("float32")
