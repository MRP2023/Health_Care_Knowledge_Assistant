# from fastapi import APIRouter, UploadFile, Depends
# from app.core.security import verify_api_key
# from app.services.embedding_service import embed_text
# from app.services.faiss_service import add_vector
# from app.utils.language_detector import detect_language

# router = APIRouter()


# @router.post("/ingest")
# async def ingest(file: UploadFile, api=Depends(verify_api_key)):

#     text = (await file.read()).decode()

#     language = detect_language(text)

#     vector = embed_text(text)

#     add_vector(vector, text, language)

#     return {"status": "stored", "language": language}

from fastapi import APIRouter, UploadFile, Depends
from app.core.security import verify_api_key
from app.services.embedding_service import embed_text
from app.services.faiss_service import add_vector
from app.utils.language_detector import detect_language

# simple function to split text by sentences


def chunk_text(text, chunk_size=200):
    sentences = text.split(". ")  # simple split, you can use nltk or spacy
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


router = APIRouter()


@router.post("/ingest")
async def ingest(file: UploadFile, api=Depends(verify_api_key)):

    text = (await file.read()).decode()

    language = detect_language(text)

    chunks = chunk_text(text, chunk_size=200)  # split into small pieces

    for chunk in chunks:
        vector = embed_text(chunk)
        add_vector(vector, chunk, language)

    return {"status": "stored", "language": language, "chunks": len(chunks)}
