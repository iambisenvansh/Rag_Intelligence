# 📄 RAG Document Intelligence System

An **end-to-end Retrieval-Augmented Generation (RAG) system** that allows users to upload PDF documents and ask contextual, citation-backed questions.

Unlike generic AI systems, this project ensures **hallucination-free, grounded responses** strictly based on uploaded documents.

> 💡 Built to demonstrate real-world GenAI engineering with focus on **accuracy, reliability, and production-ready design**

---

## 🚀 Features

- 📤 Upload PDF documents  
- 📄 Extract text using `pdfplumber`  
- ✂️ Intelligent text chunking  
- 🧠 Semantic embeddings (Sentence Transformers)  
- ⚡ Fast similarity search with FAISS  
- 🔎 Citation-aware responses (page + source tracking)  
- 💬 ChatGPT-style conversational UI  
- 🛡️ Hallucination-safe answers (strictly document-based)  
- 🌐 Full-stack implementation (FastAPI + React)  

---

## 🧠 Tech Stack

### 🔧 Backend
- FastAPI  
- pdfplumber  
- Sentence Transformers  
- FAISS  
- Pydantic  
- Python  

### 🎨 Frontend
- React (Vite)  
- Custom Chat UI  
- Fetch API  

---

## 🏗️ System Architecture

```bash
PDF Upload
   ↓
Text Extraction (pdfplumber)
   ↓
Text Chunking
   ↓
Embeddings (Sentence Transformers)
   ↓
FAISS Vector Store
   ↓
Semantic Retrieval
   ↓
Context-Grounded Answer Generation
   ↓
Response + Citations

## 📂 Project Structure

rag-doc-intelligence/
│
├── app/
│   ├── api/
│   │   ├── ingest.py        # PDF upload endpoint
│   │   ├── query.py         # Query handling
│   │   └── health.py        # Health check
│   │
│   ├── ingestion/
│   │   ├── loader.py        # PDF loader
│   │   ├── chunker.py       # Text chunking
│   │   └── embedder.py      # Embeddings
│   │
│   ├── retrieval/
│   │   ├── vector_store.py  # FAISS index
│   │   └── retriever.py     # Retrieval logic
│   │
│   ├── models/
│   │   ├── request.py
│   │   └── response.py
│   │
│   └── main.py              # Entry point
│
├── frontend/                # React UI
├── data/
│   ├── raw/                 # Uploaded PDFs
│   └── vector_store/        # FAISS index
│
├── requirements.txt
└── README.md


⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/rag-document-intelligence.git
cd rag-document-intelligence

2️⃣ Backend Setup

Create virtual environment:

python -m venv venv

Activate environment:

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run backend server:

uvicorn app.main:app --reload

📍 Backend URL: http://localhost:8000

📄 Swagger Docs: http://localhost:8000/docs

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev

📍 Frontend URL: http://localhost:5173

🧪 API Endpoints
🔹 Health Check
GET /health
🔹 Ingest PDF
POST /ingest
Content-Type: multipart/form-data
🔹 Query Document
POST /query
{
  "query": "Your question here"
}
🛡️ Hallucination Prevention
✅ Answers generated only from retrieved document context
❌ No relevant data → system refuses to answer
🔍 Ensures trustworthy, explainable AI responses
🚧 Current Limitations
Single-user local setup
Local FAISS storage
Basic answer generation (no LLM integration yet)
🔮 Future Enhancements
Multi-user & multi-document support
Reranking using cross-encoders
LLM integration (OpenAI / Gemini / Ollama)
Authentication & access control
Query analytics dashboard
Cloud vector DB (Pinecone / Qdrant)
Dockerized deployment
🎯 Why This Project Matters

This project focuses on real GenAI engineering challenges:

🔍 Retrieval correctness
🧱 System design
🛡️ Hallucination prevention
⚙️ Backend + AI integration
📦 Production-ready architecture
👨‍💻 Author

Vansh Bisen
Engineering Student | GenAI & Backend Enthusiast

🔗 LinkedIn: https://www.linkedin.com/in/vansh-bisen-80914b287/

🔗 GitHub: https://github.com/iambisenvansh

⭐ Support

If you like this project:

⭐ Star the repo
🍴 Fork it
🤝 Contribute
