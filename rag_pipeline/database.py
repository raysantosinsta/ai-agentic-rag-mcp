import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin123")
POSTGRES_DB = os.getenv("POSTGRES_DB", "agentforge")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

# String de conexão do SQLAlchemy (usada pelo LangChain)
DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
CONNECTION_STRING = DATABASE_URL # Alias comumente usado no LangChain

engine = create_engine(DATABASE_URL)

def init_db():
    """Testa a conexão e inicializa a extensão vector no PostgreSQL."""
    try:
        with engine.connect() as conn:
            # O pgvector precisa dessa extensão habilitada no banco
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            conn.commit()
        print("✅ Banco de dados conectado com sucesso e extensão 'vector' habilitada!")
    except Exception as e:
        print(f"❌ Erro ao conectar no banco de dados: {e}")

if __name__ == "__main__":
    init_db()
