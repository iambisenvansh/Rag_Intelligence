from pydantic import BaseModel
from typing import List


class Source(BaseModel):
    document: str
    page: int


class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
    confidence: float
