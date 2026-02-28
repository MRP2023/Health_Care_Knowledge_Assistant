# Healthcare RAG Assistant (Bilingual)

This project implements a Retrieval-Augmented Generation (RAG) backend for a bilingual healthcare knowledge assistant. The system allows clinicians to upload medical documents and retrieve relevant knowledge in English or Japanese.

The backend is built using FastAPI, FAISS, and Sentence Transformers with the **nomic-ai/nomic-embed-text-v1.5** embedding model.

---

## Features

- Document ingestion (.txt)
- Language detection (English/Japanese)
- Vector embeddings using BGE model
- FAISS vector search
- Top-k retrieval
- Mock LLM response generation
- Optional translation (English/Japanese)
- API Key authentication
- Docker support
- CI/CD pipeline with GitHub Actions

---

## Project Structure

```
acme-rag/
│
├── app/
│   ├── main.py
│
│   ├── api/
│   │   ├── ingest.py
│   │   ├── retrieve.py
│   │   └── generate.py
│
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│
│   ├── services/
│   │   ├── embedding_service.py
│   │   ├── faiss_service.py
│   │   ├── rag_service.py
│   │   └── translation_service.py
│
│   ├── models/
│   │   └── schemas.py
│
│   └── utils/
│       └── language_detector.py
│
├── data/
│   └── faiss_index/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .github/workflows/ci.yml
```

---

## Requirements

Python 3.10+

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Server

Activate environment:

```bash
venv\Scripts\activate
```

Start server:

```bash
uvicorn app.main:app --reload
```

Server URL:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

## API Authentication

All endpoints require an API Key.

Header:

```
X-API-Key: supersecretkey
```

---

## Endpoints

### 1. Ingest Documents

Endpoint:

```
POST /ingest
```

Description:

- Accepts .txt files
- Detects language
- Generates embeddings
- Stores in FAISS

Example upload:

```
diabetes.txt
```

Response:

```json
{
  "status": "stored",
  "language": "en"
}
```

---

### 2. Retrieve Documents

Endpoint:

```
POST /retrieve
```

Example request:

```json
{
  "query": "Type 2 diabetes treatment"
}
```

Response:

```json
[
  {
    "text": "Type 2 diabetes treatment includes diet and insulin.",
    "language": "en",
    "score": 0.42
  }
]
```

---

### 3. Generate Response

Endpoint:

```
POST /generate
```

Example request:

```json
{
  "query": "Type 2 diabetes treatment",
  "output_language": "ja"
}
```

Response:

```json
{
  "answer": "Translated response...",
  "documents": [...]
}
```

---

## Embedding Model

Model:

```
nomic-ai/nomic-embed-text-v1.5
```

Embedding Dimension:

```
768
```

---

## Running with Docker

Build container:

```bash
docker build -t healthcare-rag .
```

Run container:

```bash
docker run -p 8000:8000 healthcare-rag
```

Open:

```
http://localhost:8000/docs
```

---

## GitHub Actions CI/CD

Workflow file:

```
.github/workflows/ci.yml
```

Pipeline steps:

1. Checkout repository
2. Setup Python
3. Install dependencies
4. Verify imports

The pipeline runs automatically on push to the main branch.

---

## Setup from Scratch

Clone repository:

```bash
git clone <repository_url>
cd acme-rag
```

Create environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

---

## AI Usage Disclosure

Some code snippets and architectural guidance were assisted by AI tools and manually reviewed and modified before submission.
