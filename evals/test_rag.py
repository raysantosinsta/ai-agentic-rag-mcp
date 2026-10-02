import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def avaliar_resposta_agente(pergunta: str, resposta_agente: str, contexto_esperado: str):
    """Usa o LLM como juiz (LLM-as-a-judge) para avaliar a resposta do nosso Agente"""
    
    # LLM Avaliador (Pode ser o mesmo ou um modelo maior/diferente)
    avaliador_llm = ChatGroq(
        temperature=0, 
        model_name="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt_avaliacao = ChatPromptTemplate.from_messages([
        ("system", "Você é um Juiz de Qualidade (Evals) avaliando agentes de IA. "
                   "Sua tarefa é ler a pergunta do usuário, a resposta gerada pelo agente e o critério esperado. "
                   "Você deve retornar APENAS UMA NOTA de 0 a 10 e uma frase curta justificando."),
        ("human", "Pergunta do Usuário: {pergunta}\n\n"
                  "Resposta do Agente: {resposta}\n\n"
                  "Critério Esperado: {criterio}")
    ])

    cadeia_avaliacao = prompt_avaliacao | avaliador_llm
    
    print("⚖️  Avaliando a qualidade da resposta do Agente...")
    resultado = cadeia_avaliacao.invoke({
        "pergunta": pergunta,
        "resposta": resposta_agente,
        "criterio": contexto_esperado
    })
    
    print(f"\nResultado da Avaliação:\n{resultado.content}")

if __name__ == "__main__":
    # Simulando os dados do nosso teste anterior
    pergunta_teste = "Eu posso pedir reembolso de um livro de R$ 500 de programação?"
    resposta_agente_teste = "Sim, você pode solicitar o reembolso desse livro. De acordo com a política, o limite é de R$ 2.000 anuais."
    criterio_esperado = "O agente deve dizer que sim e citar obrigatoriamente que o limite máximo da empresa é de R$ 2.000."
    
    avaliar_resposta_agente(pergunta_teste, resposta_agente_teste, criterio_esperado)
