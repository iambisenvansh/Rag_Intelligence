import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
VECTOR_DIR = BASE_DIR / "data" / "vector_store"
INDEX_PATH = VECTOR_DIR / "index.faiss"
META_PATH = VECTOR_DIR / "metadata.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query: str, top_k: int = 5):
    if not INDEX_PATH.exists() or not META_PATH.exists():
        print("❌ Vector store files missing")
        return []

    try:
        # Load FAISS index
        index = faiss.read_index(str(INDEX_PATH))
        
        # Check if index is empty
        if index.ntotal == 0:
            print("❌ FAISS index is empty")
            return []

        # Load metadata
        with open(META_PATH, "rb") as f:
            chunks = pickle.load(f)
            
        if not chunks:
            print("❌ Metadata is empty")
            return []

        print(f"✅ Loaded index with {index.ntotal} vectors and {len(chunks)} metadata entries")

        # Embed query
        query_vector = model.encode([query])
        query_vector = np.array(query_vector).astype("float32")

        # Search
        distances, indices = index.search(query_vector, top_k)

        results = []
        for score, idx in zip(distances[0], indices[0]):
            if idx < len(chunks):  # Safety check
                chunk = chunks[idx]
                results.append({
                    "text": chunk["text"],
                    "page": chunk["page"],
                    "source": chunk["source"],
                    "score": float(score)
                })

        print(f"✅ Retrieved {len(results)} chunks")
        return results
        
    except Exception as e:
        print(f"❌ Retrieval error: {e}")
        return []
