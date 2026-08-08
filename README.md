# 📄 RAG Document Intelligence System

An **end-to-end Retrieval-Augmented Generation (RAG) system** that allows users to upload PDF documents and ask contextual, citation-backed questions.

Unlike generic AI systems, this project is designed to provide **grounded responses based strictly on uploaded documents**.

> 💡 Built to demonstrate real-world GenAI engineering with a focus on **accuracy, reliability, and production-ready design**.

---

## 🚀 Features

- 📤 Upload PDF documents
- 📄 Extract text using `pdfplumber`
- ✂️ Intelligent text chunking
- 🧠 Semantic embeddings using Sentence Transformers
- ⚡ Fast similarity search using FAISS
- 🔎 Citation-aware responses with page and source tracking
- 💬 ChatGPT-style conversational UI
- 🛡️ Hallucination-safe, document-grounded answers
- 🌐 Full-stack implementation using FastAPI and React

---

## 🧠 Tech Stack

### 🔧 Backend

- Python
- FastAPI
- pdfplumber
- Sentence Transformers
- FAISS
- Pydantic

### 🎨 Frontend

- React
- Vite
- Fetch API
- Custom Chat UI

---

## 🏗️ System Architecture

```text
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


## Project Structure

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
│   └── main.py              # FastAPI entry point
│
├── frontend/
│   └── React UI
│
├── data/
│   ├── raw/                 # Uploaded PDFs
│   └── vector_store/        # FAISS index
│
├── requirements.txt
├── Dockerfile
└── README.md