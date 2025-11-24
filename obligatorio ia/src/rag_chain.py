import os
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from src.vector_store import load_vector_store

def get_rag_chain(api_key=None):
 
    if not api_key:
        raise ValueError("No API key provided")

    llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0, api_key=api_key)
    store = load_vector_store()
    retriever = store.as_retriever(search_kwargs={"k": 1000})

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )
    return chain
