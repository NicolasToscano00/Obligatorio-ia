
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

VECTOR_DIR = Path("vector_store")

def build_and_save_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.from_texts(docs, embeddings)
    VECTOR_DIR.mkdir(exist_ok=True)
    store.save_local(str(VECTOR_DIR))

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(str(VECTOR_DIR), embeddings,  allow_dangerous_deserialization=True)
