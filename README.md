# VertoArc - Seu Mentor de Carreira com IA

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-green.svg)
![Docker](https://img.shields.io/badge/Docker-blue.svg)

**VertoArc** é uma ferramenta de IA projetada para atuar como um mentor de carreira, ajudando profissionais a otimizar seus currículos para vagas de emprego específicas. Utilizando o poder do Google Gemini, o VertoArc analisa o seu perfil contra a descrição de uma vaga e fornece feedback instantâneo, acionável e personalizado.

## O Problema

Muitos profissionais talentosos perdem oportunidades por não conseguirem comunicar de forma eficaz como suas habilidades e experiências se alinham com os requisitos de uma vaga. O VertoArc visa preencher essa lacuna, oferecendo uma análise inteligente que normalmente só seria acessível através de um recrutador experiente.

## Status do Projeto

O projeto está atualmente na **Fase 2 de desenvolvimento**. O núcleo da aplicação está funcional, com uma API RESTful capaz de processar análises via IA. As próximas fases se concentrarão em persistência de dados, testes e na criação de uma interface de usuário.

## Funcionalidades Atuais

* **Endpoint `/analyze`:** Recebe o texto de um currículo e de uma vaga via `POST`.
* **Análise com IA:** Integra-se com a API do Google Gemini para gerar uma análise completa, incluindo:
    * Score de compatibilidade (%) com justificativa.
    * Pontos fortes do candidato para a vaga.
    * Sugestões de melhoria específicas e acionáveis para o currículo.
    * Perguntas de entrevista (técnicas e comportamentais) baseadas no perfil.
* **Ambiente Containerizado:** A aplicação e seus serviços são totalmente gerenciados com Docker e Docker Compose, garantindo um ambiente de desenvolvimento consistente e replicável.

## Stack Tecnológica

* **Backend:** Python
* **Framework API:** FastAPI
* **Validação de Dados:** Pydantic
* **Inteligência Artificial:** Google Gemini API
* **Containerização:** Docker & Docker Compose

## Como Executar Localmente

Para rodar o projeto em seu ambiente local, siga os passos abaixo.

**Pré-requisitos:**
* [Docker](https://www.docker.com/products/docker-desktop/) instalado.
* Uma chave de API do Google Gemini.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_AQUI]
    cd VertoArc
    ```

2.  **Crie o arquivo de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:
    ```.env
    GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
    ```
    Substitua `SUA_CHAVE_API_AQUI` pela sua chave de API do Google Gemini.

3.  **Construa e suba os containers:**
    Execute o seguinte comando na raiz do projeto.
    ```bash
    docker-compose up --build
    ```

4.  **Acesse a API:**
    A API estará disponível em `http://127.0.0.1:8000`.
    A documentação interativa (Swagger UI) pode ser acessada em `http://127.0.0.1:8000/docs`.

## Roadmap do Projeto

Abaixo estão os próximos passos planejados para o desenvolvimento do VertoArc:

-   [ ] **Fase 3: Persistência de Dados**
    -   [ ] Integração com PostgreSQL para salvar análises.
    -   [ ] Implementação de modelos de dados com SQLAlchemy.
    -   [ ] Gerenciamento de schema do banco com Alembic.
-   [ ] **Fase 4: Testes**
    -   [ ] Implementação de testes unitários e de integração com Pytest.
-   [ ] **Fase 5: Interface de Usuário**
    -   [ ] Criação de uma UI simples com Streamlit para facilitar o uso da ferramenta.

## Contribuição

Este é um projeto de portfólio em desenvolvimento. Sugestões e feedbacks construtivos são muito bem-vindos! Sinta-se à vontade para abrir uma *Issue* no GitHub.
