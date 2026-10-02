import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.pgvector import PGVector
from dotenv import load_dotenv

# Carregar variáveis do .env

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin123")
POSTGRES_DB = os.getenv("POSTGRES_DB", "agentforge")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

CONNECTION_STRING = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
COLLECTION_NAME = "corporate_docs"

def ingest_documents():
    print("📥 Iniciando a ingestão de documentos...")
    
    # 1. Carregar documentos (Vamos criar um texto de exemplo no código para testar)
    sample_text = """
    A AgentForge Inc. adota uma política de tolerância zero com violações de dados. 
    Todos os acessos aos servidores de produção devem ser feitos exclusivamente via VPN com autenticação multifator (MFA).
    O suporte de TI nível 1 atende pelo ramal 9900 ou email ti@agentforge.com.br.
    Reembolsos de cursos e livros técnicos são limitados a R$ 2.000 anuais por funcionário.
    """
    
    # Salvar temporariamente para o Loader ler
    file_path = "temp_doc.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(sample_text.strip())
        
    loader = TextLoader(file_path, encoding="utf-8")
    docs = loader.load()

    # 2. Chunking (quebrar em pedaços menores)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)
    splits = text_splitter.split_documents(docs)
    print(f"🧩 Documento dividido em {len(splits)} pedaços (chunks).")

    # 3. Gerar Embeddings e salvar no pgvector
    print("🧠 Gerando embeddings locais (HuggingFace) e salvando no PostgreSQL...")
    # Usaremos um modelo leve e open-source para embeddings já que o Groq não os fornece
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Instancia e salva os vetores
    PGVector.from_documents(
        embedding=embeddings,
        documents=splits,
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
    )
    
    print("✅ Ingestão finalizada com sucesso! Textos vetorizados e guardados no pgvector.")
    
    # Limpeza
    os.remove(file_path)

if __name__ == "__main__":
    ingest_documents()
