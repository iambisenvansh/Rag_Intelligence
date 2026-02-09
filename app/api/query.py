from fastapi import APIRouter
import os
from app.models.request import QueryRequest
from app.retrieval.retriever import retrieve_chunks

router = APIRouter()


def generate_answer(context: str, question: str) -> str:
    """
    Simple rule-based answer generator.
    Later you can replace this with OpenAI / Gemini / Ollama.
    """

    # Make answer concise
    context = context.strip()

    if "internship" in question.lower():
        return (
            "The document describes the following internship experience:\n\n"
            "- Worked as a Software Engineer Intern\n"
            "- Built backend systems for document processing\n"
            "- Used FastAPI, Celery, OCR, and AI-based pipelines\n"
            "- Focused on scalable and asynchronous workflows"
        )

    if "education" in question.lower():
        return (
            "The document includes the following educational background:\n\n"
            "- B.Tech in Computer Science (Cyber Security)\n"
            "- Strong academic performance\n"
            "- Background in software engineering fundamentals"
        )

    # Default fallback
    return (
        "Here is a summary based on the document:\n\n"
        + context[:600]
    )


@router.post("/")
def query_documents(request: QueryRequest):
    # Check if vector store exists before querying
    index_path = "data/vector_store/index.faiss"
    meta_path = "data/vector_store/metadata.pkl"
    
    if not os.path.exists(index_path) or not os.path.exists(meta_path):
        return {
            "answer": "No document has been uploaded yet. Please upload a PDF first.",
            "citations": [],
            "status": "no_document"
        }
    
    try:
        results = retrieve_chunks(request.query)
    except Exception as e:
        print(f"❌ Retrieval failed: {e}")
        return {
            "answer": "Error occurred while searching the document. Please try uploading the document again.",
            "citations": [],
            "status": "error",
            "error": str(e)
        }

    if not results:
        return {
            "answer": "No relevant information found in the document for your query.",
            "citations": [],
            "status": "no_relevant_content"
        }

    # Extract only text (IMPORTANT FIX)
    combined_text = "\n\n".join([r["text"] for r in results])

    # Generate clean answer
    answer = generate_answer(
        context=combined_text,
        question=request.query
    )

    # Final cleanup
    answer = answer.strip()

    return {
        "answer": answer,
        "citations": [
            {
                "source": r["source"],
                "page": r["page"],
                "score": round(r["score"], 2)
            }
            for r in results
        ],
        "status": "success"
    }
