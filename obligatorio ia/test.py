from src.load_data import load_dataset
from src.build_corpus import build_documents
from src.vector_store import build_and_save_vector_store
import os

df = load_dataset()
docs = build_documents(df)
build_and_save_vector_store(docs)

print("Vector store generado con", len(docs), "documentos")
