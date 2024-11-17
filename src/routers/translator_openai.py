from src.models.translator import TranslatorToFrench
from fastapi import APIRouter
from transformers import pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

key_api_openai = os.environ["OPENAI_KEY"]
model_gpt_35= 'gpt-3.5-turbo'

router = APIRouter()

def translator_to_french_openai(text: str):
    """
    Traduz uma frase em português para inglês
    """
    template = ChatPromptTemplate([
        ('system','Você é um tradutor de frases em inglês para francês'),
        ('user','Traduza isso: {text}')
    ])
    llm = ChatOpenAI(model = model_gpt_35,api_key=key_api_openai)
    response = llm.invoke(template.format_messages(text = text))
    return response

@router.post('/translator_openai/')
async def chat(body: TranslatorToFrench):
    response = translator_to_french_openai(body.message)
    return {'assistant': response.content}