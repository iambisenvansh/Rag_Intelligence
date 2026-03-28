📄 RAG Document Intelligence System

An end-to-end Retrieval-Augmented Generation (RAG) system that enables users to upload PDF documents and ask contextual, citation-backed questions.

Unlike generic AI chat systems, this solution ensures grounded, hallucination-free responses strictly based on the uploaded documents.

💡 Designed to demonstrate real-world GenAI engineering with a focus on accuracy, reliability, and production-ready architecture

🚀 Key Features
📤 Upload and process PDF documents
📄 Accurate text extraction using pdfplumber
✂️ Intelligent text chunking for better retrieval
🧠 Semantic embeddings via Sentence Transformers
⚡ Fast vector similarity search with FAISS
🔎 Citation-aware answers (page + source tracking)
💬 ChatGPT-like conversational interface
🛡️ Hallucination-safe responses (strictly document-based)
🌐 Full-stack implementation (FastAPI + React)


🧠 Tech Stack

🔧 Backend

FastAPI – High-performance API framework
pdfplumber – PDF text extraction
Sentence Transformers – Semantic embeddings
FAISS – Vector similarity search
Pydantic – Data validation
Python

🎨 Frontend

React (Vite) – Fast modern UI
Custom Chat Interface
Fetch API – API communication



🏗️ System Architecture

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

📂 Project Structure

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

Activate it:

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn app.main:app --reload

📍 Backend runs at:
👉 http://localhost:8000

📄 API Docs (Swagger):
👉 http://localhost:8000/docs

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev

📍 Frontend runs at:
👉 http://localhost:5173

🧪 API Endpoints
🔹 Health Check
GET /health
🔹 Upload & Ingest PDF
POST /ingest
Content-Type: multipart/form-data
🔹 Query Documents
POST /query
{
  "query": "Your question here"
}

🛡️ Hallucination Prevention
✅ Answers are generated only from retrieved document context
❌ If no relevant data is found → system refuses to answer
🔍 Ensures trustworthy, explainable AI responses

🚧 Current Limitations
Single-user (local environment)
Local FAISS storage

Basic answer generation (no LLM yet)
🔮 Future Enhancements
✅ Multi-user & multi-document support
🔄 Reranking using cross-encoders
🤖 LLM integration (OpenAI / Gemini / Ollama)
🔐 Authentication & access control
📊 Query analytics dashboard
☁️ Cloud vector DB (Pinecone / Qdrant)
🐳 Dockerized deployment
🎯 Why This Project Stands Out

This is not just a demo — it addresses real GenAI engineering challenges:

🔍 Retrieval accuracy
🧱 System design & scalability
🛡️ Hallucination prevention
📦 Production-ready architecture
⚙️ Backend + AI integration
👨‍💻 Author

Vansh Bisen
Engineering Student | GenAI & Backend Enthusiast

🔗 LinkedIn: https://www.linkedin.com/in/vansh-bisen-80914b287/

🔗 GitHub: https://github.com/iambisenvansh
