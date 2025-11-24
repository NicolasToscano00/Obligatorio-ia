set -e


python -m pip install -r requirements.txt


# 2) Exportar API KEY (o usar .env)
export OPENAI_API_KEY=$(grep OPENAI_API_KEY .env | cut -d'=' -f2-)


python - <<PY
from src.load_data import load_dataset
from src.build_corpus import build_documents
from src.vector_store import build_and_save_vector_store
import os


api_key = os.getenv('OPENAI_API_KEY')


df = load_dataset()
docs = build_documents(df)
print('Docs:', len(docs))
build_and_save_vector_store(docs, api_key)
PY


uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload