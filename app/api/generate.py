from fastapi import APIRouter, Depends
from app.core.security import verify_api_key
from app.models.schemas import QueryRequest
from app.services.rag_service import generate_answer
from app.services.translation_service import translate

router = APIRouter()


@router.post("/generate")
def generate(data: QueryRequest, api=Depends(verify_api_key)):

    answer, docs = generate_answer(data.query)

    if data.output_language:

        answer = translate(answer, data.output_language)

    return {
        "answer": answer,
        "documents": docs
    }
