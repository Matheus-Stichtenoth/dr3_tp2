from src.models.translator_germany import TranslatorToGermany
from fastapi import APIRouter
from transformers import pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()

api_key_hugging_face = os.environ['HUGGINGFACE_HUB_API_TOKEN']
model_translator = 'Helsinki-NLP/opus-mt-en-de'

router = APIRouter()

def translator_to_germany(message:str):
    """
    Traduz um texto em inglês para alemão
    """
    llm = HuggingFaceHub(
        repo_id = model_translator,
        huggingfacehub_api_token = api_key_hugging_face
    )
    response = llm.invoke(message)
    return response

@router.post('/translator_germany/')
async def chat(body: TranslatorToGermany):
    response = translator_to_germany(body.message)
    return {'assistant': response}