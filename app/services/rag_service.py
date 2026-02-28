from app.services.embedding_service import embed_text
from app.services.faiss_service import search


def generate_answer(query):

    vector = embed_text(query)

    docs = search(vector)

    context = " ".join([d["text"] for d in docs])

    answer = f"""
Query:
{query}

Relevant information:
{context}

Summary:
Based on retrieved documents, the recommended approach is described above.
"""

    return answer, docs
