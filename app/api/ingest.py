from fastapi import APIRouter, UploadFile, File
import shutil
import os
import shutil

from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import embed_chunks
from app.retrieval.vector_store import store_embeddings

router = APIRouter()

UPLOAD_DIR = "data/raw"
VECTOR_DIR = "data/vector_store"


@router.post("/")
async def ingest_documents(file: UploadFile = File(...)):
    try:
        # 1️⃣ Ensure folders exist
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        os.makedirs(VECTOR_DIR, exist_ok=True)

        # 2️⃣ CLEAR OLD VECTOR STORE (IMPORTANT) - Safe cleanup
        if os.path.exists(VECTOR_DIR):
            for f in os.listdir(VECTOR_DIR):
                file_path = os.path.join(VECTOR_DIR, f)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        
        print(f"✅ Directories created: {UPLOAD_DIR}, {VECTOR_DIR}")
    except Exception as e:
        print(f"❌ Directory setup failed: {e}")
        return {"error": f"Failed to setup directories: {str(e)}", "chunks_created": 0}

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # 3️⃣ Save uploaded file
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"✅ File saved: {file_path}")
    except Exception as e:
        print(f"❌ File save failed: {e}")
        return {"error": f"Failed to save file: {str(e)}", "chunks_created": 0}

    # 4️⃣ Extract text
    try:
        text = load_pdf(file_path)
        print("📄 Document:", file.filename)
        print("📏 Extracted text length:", len(text))
    except Exception as e:
        print(f"❌ PDF extraction failed: {e}")
        return {"error": f"Failed to extract PDF text: {str(e)}", "chunks_created": 0}

    if len(text.strip()) < 200:
        return {
            "error": "PDF contains very little readable text (less than 200 characters)",
            "message": "PDF contains very little readable text",
            "chunks_created": 0,
        }

    # 5️⃣ Chunk text
    try:
        raw_chunks = chunk_text(text)
        print(f"📝 Created {len(raw_chunks)} chunks")
    except Exception as e:
        print(f"❌ Chunking failed: {e}")
        return {"error": f"Failed to chunk text: {str(e)}", "chunks_created": 0}

    if not raw_chunks:
        return {"error": "No chunks created from document", "message": "No chunks created from document", "chunks_created": 0}

    # 6️⃣ Attach metadata
    chunks = [
        {"text": chunk, "page": i + 1, "source": file.filename}
        for i, chunk in enumerate(raw_chunks)
    ]

    # 7️⃣ Embed text
    try:
        embeddings = embed_chunks([c["text"] for c in chunks])
        print("🧠 Embeddings shape:", embeddings.shape)
    except Exception as e:
        print(f"❌ Embedding failed: {e}")
        return {"error": f"Failed to generate embeddings: {str(e)}", "chunks_created": 0}

    # 8️⃣ Store vectors + metadata
    try:
        store_embeddings(embeddings, chunks)
        print("💾 Vector store saved successfully")
        
        # Verify files were created
        index_path = os.path.join("data", "vector_store", "index.faiss")
        meta_path = os.path.join("data", "vector_store", "metadata.pkl")
        
        if not os.path.exists(index_path) or not os.path.exists(meta_path):
            return {"error": "Vector store files were not created properly", "chunks_created": 0}
            
        print(f"✅ Verified: {index_path} and {meta_path} exist")
        
    except Exception as e:
        print(f"❌ Vector store save failed: {e}")
        return {"error": f"Failed to save vector store: {str(e)}", "chunks_created": 0}

    return {
        "message": "Document ingested successfully",
        "document": file.filename,
        "chunks_created": len(chunks),
    }
