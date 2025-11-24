from fastapi import FastAPI
from pydantic import BaseModel
import os
from src.rag_chain import get_rag_chain

from dotenv import load_dotenv
load_dotenv()

class Query(BaseModel):
    question: str

app = FastAPI()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_KEY:
    raise ValueError("Falta la variable OPENAI_API_KEY")

chain = get_rag_chain(api_key=OPENAI_KEY)


@app.post("/chat")
def chat(q: Query):
    result = chain(q.question)
    return {
        "answer": result["result"],
        "sources": [str(d.page_content[:200]) for d in result["source_documents"]]
    }

