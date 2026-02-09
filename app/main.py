from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ingest, query, health

app = FastAPI(
    title="RAG Document Intelligence API",
    version="1.0.0"
)

# ✅ CORS middleware (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API routes
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(ingest.router, prefix="/ingest", tags=["Ingestion"])
app.include_router(query.router, prefix="/query", tags=["Query"])
