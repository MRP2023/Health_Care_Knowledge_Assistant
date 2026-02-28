import faiss
import numpy as np
import pickle
import os
from app.core.config import FAISS_PATH, METADATA_PATH

dimension = 768

# Ensure directories exist
os.makedirs(os.path.dirname(FAISS_PATH), exist_ok=True)
os.makedirs(os.path.dirname(METADATA_PATH), exist_ok=True)

if os.path.exists(FAISS_PATH):
    index = faiss.read_index(FAISS_PATH)
    with open(METADATA_PATH, "rb") as f:
        metadata = pickle.load(f)
else:
    index = faiss.IndexFlatL2(dimension)
    metadata = []

def save():
    # Ensure directories exist (extra safety)
    os.makedirs(os.path.dirname(FAISS_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(METADATA_PATH), exist_ok=True)

    faiss.write_index(index, FAISS_PATH)
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)

def add_vector(vector, text, language):
    vector = np.array([vector]).astype("float32")
    index.add(vector)

    metadata.append({
        "text": text,
        "language": language
    })

    save()

def search(vector, k=3):
    vector = np.array([vector]).astype("float32")
    distances, indices = index.search(vector, k)

    results = []
    for i, d in zip(indices[0], distances[0]):
        if i < len(metadata):
            results.append({
                "text": metadata[i]["text"],
                "language": metadata[i]["language"],
                "score": float(d)
            })
    return results