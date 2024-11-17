from fastapi import APIRouter, HTTPException
from src.models.question import QuestionFixed

# Inicializa o roteador para perguntas
router = APIRouter()

# Dicionário de mapeamento pergunta → resposta
qa_mapping = {
    "Olá": "Olá! Como posso ajudar você hoje?",
    "Qual é o seu nome?": "Eu sou um chatbot simulado!",
    "O que você faz?": "Eu sou apenas um protótipo que responde perguntas simples.",
    "Tchau": "Até logo! Foi um prazer falar com você.",
}

# Classe simulando um LLM com respostas fixas
class FixedResponseLLM:
    def predict(self, input_text: str) -> str:
        # Retorna a resposta associada à pergunta ou uma mensagem padrão
        return qa_mapping.get(input_text, "Desculpe, não entendi sua pergunta.")

# Instancia o modelo com as respostas fixas
fake_llm = FixedResponseLLM()

# Endpoint para responder perguntas
@router.post("/ask/")
async def ask_question(question: QuestionFixed):
    user_input = question.question.strip()
    # Obtém a resposta do modelo customizado
    response = fake_llm.predict(user_input)
    
    if response == "Desculpe, não entendi sua pergunta.":
        # Retorna um erro para perguntas não reconhecidas
        raise HTTPException(status_code=404, detail="Pergunta não reconhecida.")
    
    return {"response": response}