from mcp.server.mcpserver import MCPServer

# Inicializa o servidor MCPServer (wrapper oficial para Python v2)
# O MCPServer suporta comunicação via STDIO (padrão) e SSE/HTTP
mcp = MCPServer("AgentForge")

# Ferramenta 1: Leitura de políticas corporativas
@mcp.tool()
def read_corporate_policy(topic: str) -> str:
    """
    Recupera informações sobre políticas corporativas da empresa.
    Tópicos válidos: 'home_office', 'reembolso', 'seguranca'.
    """
    policies = {
        "home_office": "A política de home office permite até 3 dias remotos na semana (terça a quinta).",
        "reembolso": "Reembolsos de viagens devem ser solicitados em até 5 dias úteis com NF anexa. Limite diário de refeição é R$100.",
        "seguranca": "Senhas devem ser trocadas a cada 90 dias e ter mínimo de 14 caracteres."
    }
    
    return policies.get(
        topic.lower(), 
        f"Política para o tópico '{topic}' não encontrada. Tópicos disponíveis: {', '.join(policies.keys())}."
    )

# Ferramenta 2: Consulta de chamados de suporte (Simulação)
@mcp.tool()
def check_support_ticket(ticket_id: int) -> str:
    """
    Consulta o status de um chamado de suporte de TI (simulado).
    """
    tickets = {
        101: {"status": "Aberto", "description": "Problema de acesso ao banco de dados pgvector."},
        102: {"status": "Resolvido", "description": "Troca de teclado e mouse."},
        103: {"status": "Em Andamento", "description": "Configuração da VPN para novo colaborador."}
    }
    
    ticket = tickets.get(ticket_id)
    if ticket:
        return f"Chamado #{ticket_id}: Status='{ticket['status']}' | Descrição='{ticket['description']}'"
    return f"Chamado #{ticket_id} não encontrado no sistema."


if __name__ == "__main__":
    # Inicia o servidor MCP. Por padrão, ele ouve no stdio (entrada e saída padrão),
    # que é a forma recomendada para LLMs/Agentes rodando localmente se comunicarem.
    mcp.run()
