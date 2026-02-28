# from sentence_transformers import SentenceTransformer
# from app.core.config import EMBEDDING_MODEL

# model = SentenceTransformer(EMBEDDING_MODEL)


# def embed_text(text: str):
#     text = "Represent this sentence for searching: " + text
#     return model.encode(text, normalize_embeddings=True)


# app/services/embedding_service.py
from sentence_transformers import SentenceTransformer
from app.core.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL, trust_remote_code=True)


def embed_text(text: str):
    """Single-text embedding (compatible with old code)"""
    text = "Represent this sentence for searching: " + text
    return model.encode(text, normalize_embeddings=True)


def embed_query(text: str):
    text = "Represent this sentence for searching: " + text
    return model.encode(text, normalize_embeddings=True)


def embed_documents(texts: list[str]):
    return model.encode(texts, normalize_embeddings=True)
