import faiss
import pickle
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
VECTOR_DIR = BASE_DIR / "data" / "vector_store"
INDEX_PATH = VECTOR_DIR / "index.faiss"
META_PATH = VECTOR_DIR / "metadata.pkl"

def store_embeddings(embeddings, chunks):
    try:
        VECTOR_DIR.mkdir(parents=True, exist_ok=True)
        print(f"✅ Vector directory created: {VECTOR_DIR}")

        embeddings = np.array(embeddings).astype("float32")
        print(f"✅ Embeddings prepared: shape {embeddings.shape}")

        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)

        index.add(embeddings)
        print(f"✅ Added {embeddings.shape[0]} vectors to FAISS index")

        # Write index
        faiss.write_index(index, str(INDEX_PATH))
        print(f"✅ FAISS index saved to: {INDEX_PATH}")

        # Write metadata
        with open(META_PATH, "wb") as f:
            pickle.dump(chunks, f)
        print(f"✅ Metadata saved to: {META_PATH}")
        
        # Verify files exist and have content
        if INDEX_PATH.exists() and META_PATH.exists():
            index_size = INDEX_PATH.stat().st_size
            meta_size = META_PATH.stat().st_size
            print(f"✅ Verification: index.faiss ({index_size} bytes), metadata.pkl ({meta_size} bytes)")
        else:
            raise Exception("Vector store files were not created")
            
    except Exception as e:
        print(f"❌ Vector store creation failed: {e}")
        raise e
