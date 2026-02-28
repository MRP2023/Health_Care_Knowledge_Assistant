from fastapi import FastAPI
from app.api import ingest, retrieve, generate

app = FastAPI(
    title="Healthcare RAG Assistant",
    description="Bilingual Medical Knowledge Assistant",
    version="1.0"
)

app.include_router(ingest.router)
app.include_router(retrieve.router)
app.include_router(generate.router)


@app.get("/")
def root():
    return {"message": "Healthcare RAG Assistant Running"}
