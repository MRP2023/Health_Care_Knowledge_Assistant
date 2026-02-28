from fastapi import APIRouter, Depends
from app.core.security import verify_api_key
from app.models.schemas import QueryRequest
from app.services.embedding_service import embed_text
from app.services.faiss_service import search

router = APIRouter()


@router.post("/retrieve")
def retrieve(data: QueryRequest, api=Depends(verify_api_key)):

    vector = embed_text(data.query)

    results = search(vector)

    return results
