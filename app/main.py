from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ingest, query, health

app = FastAPI(
    title="RAG Document Intelligence API",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "RAG Document Intelligence API Running"
    }

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    ingest.router,
    prefix="/ingest",
    tags=["Ingestion"]
)

app.include_router(
    query.router,
    prefix="/query",
    tags=["Query"]
)
