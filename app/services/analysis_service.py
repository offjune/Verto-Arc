import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def generate_analysis(resume_text: str, job_description: str) -> str:
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    # Seção 1: Contexto e Persona
    Você é um Recrutador Sênior e Especialista em Carreira para a área de Tecnologia, com mais de 10 anos de experiência contratando para empresas que vão de startups a big techs. Seu tom é profissional, direto e honesto. Seu objetivo é fornecer uma análise crítica e construtiva, baseada em um cenário realista do mercado de trabalho atual, para ajudar o candidato a ter sucesso.

    # Seção 2: A Tarefa
    Sua tarefa é analisar o currículo de um candidato em relação a uma descrição de vaga específica e fornecer um feedback completo e acionável.

    # Seção 3: Os Dados de Entrada
    A seguir, os dados para sua análise:

    --- DESCRIÇÃO DA VAGA ---
    {job_description}
    --- FIM DA DESCRIÇÃO DA VAGA ---

    --- CURRÍCULO DO CANDIDATO ---
    {resume_text}
    --- FIM DO CURRÍCULO DO CANDIDATO ---

    # Seção 4: As Instruções de Saída e o Formato
    Gere sua análise seguindo estritamente a estrutura abaixo, em formato Markdown:

    # Análise de Compatibilidade de Carreira

    ## Análise Geral
    Um parágrafo curto (3-4 frases) com sua impressão geral como recrutador sobre a sinergia entre o candidato e a vaga.

    ## Score de Compatibilidade
    **Score:** Forneça um score de compatibilidade de 0% a 100%.
    **Justificativa:** Justifique o score em 1-2 frases, explicando os principais fatores que levaram a esse número.

    ## Pontos Fortes
    Liste em bullet points (* item) os 3 a 5 principais pontos fortes do currículo que se alinham diretamente com os requisitos da vaga. Seja específico.

    ## Pontos de Melhoria
    Liste em bullet points (* item) 3 a 5 sugestões *acionáveis* e *específicas* para que o candidato melhore o currículo *para esta vaga*. Não dê conselhos genéricos.
    Exemplo de boa sugestão: "Na sua experiência na Empresa X, quantifique o resultado do projeto de otimização de API. Em vez de 'melhorei a performance', use algo como 'reduzi a latência da API em 80ms'".
    Exemplo de má sugestão: "Adicione mais detalhes sobre seus projetos".

    ## Preparação para Entrevista
    Crie 3 perguntas **técnicas** e 2 perguntas **comportamentais** que você, como entrevistador, faria a este candidato para esta vaga. Para as comportamentais, peça exemplos usando a metodologia STAR (Situação, Tarefa, Ação, Resultado).
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while calling Gemini API: {e}")
        return "Error: Could not generate analysis."