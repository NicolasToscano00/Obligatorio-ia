from dotenv import load_dotenv
from pathlib import Path

def load_env(path='.env'):
    p = Path(path)
    if p.exists():
        load_dotenv(p)
    else:
        print(f"No se encontró {path}. Copiá .env.txt a .env y completá la OPENAI_API_KEY")