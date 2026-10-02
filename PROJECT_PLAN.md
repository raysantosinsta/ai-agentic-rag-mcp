# AgentForge MCP - Plano de Execução do Projeto

Este plano de projeto foi desenhado para criar uma Plataforma de Orquestração de Agentes com RAG e MCP, ideal para demonstrar habilidades avançadas em Engenharia de IA Generativa.

## Fases do Projeto

### Fase 1: Configuração Inicial e Arquitetura Básica
*   **Objetivo:** Estabelecer a base do projeto, ferramentas de qualidade de código e estrutura de pastas.
*   **Tarefas:**
    1.  Inicializar repositório Git.
    2.  Configurar ambiente virtual Python (ex: `venv` ou `poetry`).
    3.  Instalar dependências iniciais (`langchain`, `langgraph` ou `crewai`, `pydantic`, `fastapi`, etc.).
    4.  Criar a estrutura de diretórios (`/agents`, `/mcp-server`, `/rag-pipeline`, `/evals`).
    5.  Configurar linters e formatadores (Ruff, Black, Mypy).

### Fase 2: Implementação do Servidor MCP (Model Context Protocol)
*   **Objetivo:** Criar um servidor local para expor ferramentas e dados de forma padronizada.
*   **Tarefas:**
    1.  Desenvolver o servidor MCP básico.
    2.  Implementar ferramentas (tools) no MCP (ex: leitura de arquivos locais, consulta simulada a um banco de dados).
    3.  Testar a conexão do servidor MCP de forma isolada.

### Fase 3: Pipeline de RAG Avançado
*   **Objetivo:** Criar o sistema de ingestão e busca vetorial.
*   **Tarefas:**
    1.  Subir um banco vetorial local via Docker (ex:  pgvector).
    2.  Desenvolver script de ingestão de documentos (chunking com LangChain, geração de embeddings).
    3.  Implementar a lógica de busca semântica (Retriever).
    4.  Expor a ferramenta de busca via servidor MCP.

### Fase 4: Esteiras Agênticas e Skills
*   **Objetivo:** Desenvolver os agentes autônomos que utilizarão o RAG e o MCP.
*   **Tarefas:**
    1.  Definir a arquitetura multi-agente (ex: usando LangGraph para fluxos controlados).
    2.  Criar as Skills (classes modulares).
    3.  Configurar os agentes para consumirem as ferramentas do servidor MCP.
    4.  Implementar um caso de uso corporativo completo (ex: agente auditor recebendo um documento, buscando contexto no RAG e analisando problemas).

### Fase 5: Observabilidade e Avaliação (Evals)
*   **Objetivo:** Garantir a qualidade, rastreabilidade e métricas da solução.
*   **Tarefas:**
    1.  Integrar ferramenta de observabilidade (ex: LangSmith, Arize Phoenix ou OpenInference) para rastrear custos de tokens e steps dos agentes.
    2.  Criar scripts em `/evals` usando a técnica *LLM-as-a-judge* para avaliar a precisão das respostas do agente com base no contexto recuperado.

### Fase 6: Documentação e Dockerização
*   **Objetivo:** Preparar o projeto para o portfólio.
*   **Tarefas:**
    1.  Criar `Dockerfile` e `docker-compose.yml` para facilitar a execução.
    2.  Escrever um `README.md` abrangente, incluindo diagramas de arquitetura (Mermaid), instruções de uso e explicação de como o projeto atende aos requisitos de mercado.

## Próximos Passos Sugeridos
Podemos começar executando a **Fase 1**. Gostaria que eu criasse a estrutura de pastas e os arquivos de configuração iniciais (como `requirements.txt` e a estrutura de diretórios) aqui no workspace?
