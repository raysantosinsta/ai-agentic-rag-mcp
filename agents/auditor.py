import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.pgvector import PGVector
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# 1. Configurações Iniciais
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin123")
POSTGRES_DB = os.getenv("POSTGRES_DB", "agentforge")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
CONNECTION_STRING = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

llm = ChatGroq(
    temperature=0, 
    model_name="openai/gpt-oss-120b", # Modelo atual que existe no Groq 
    api_key=os.getenv("GROQ_API_KEY")
)

# 3. Configurar a conexão com o nosso RAG (pgvector)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = PGVector(
    connection_string=CONNECTION_STRING,
    embedding_function=embeddings,
    collection_name="corporate_docs"
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 4. Criar a "Skill" (Ferramenta) de Busca de Políticas usando o RAG
@tool
def busca_politicas_empresa(query: str) -> str:
    """Busca e retorna informações sobre as regras e políticas da empresa (ex: reembolso, home office, segurança). Use isso sempre que precisar responder sobre as regras da AgentForge."""
    # O retriever busca no pgvector os chunks mais relevantes
    docs = retriever.invoke(query)
    # Formata os resultados em um único texto para o Agente ler
    return "\n\n".join([doc.page_content for doc in docs])

tools = [busca_politicas_empresa]

# 5. Configurar o Agente Auditor usando LangGraph (Módulo super em alta no mercado)
instrucoes_sistema = (
    "Você é um Agente Auditor de TI Sênior da empresa AgentForge. "
    "Seu trabalho é ajudar os funcionários a tirarem dúvidas sobre as regras da empresa. "
    "Sempre busque a informação nas políticas da empresa usando a ferramenta antes de responder. "
    "Seja educado, analítico e responda em português do Brasil."
)

agent = create_react_agent(llm, tools=tools)

if __name__ == "__main__":
    print("🤖 Iniciando Agente Auditor com Groq Llama-3 e RAG via LangGraph...")
    
    pergunta_usuario = "Eu posso pedir reembolso de um livro de R$ 500 de programação?"
    print(f"\nUsuário: {pergunta_usuario}\n")
    
    # Executar o grafo do LangGraph passando o system prompt diretamente na mensagem
    resultado = agent.invoke({"messages": [
        ("system", instrucoes_sistema),
        ("user", pergunta_usuario)
    ]})
    
    # A última mensagem do grafo é a resposta final do agente
    resposta = resultado["messages"][-1].content
    print(f"\nAgente: {resposta}")
