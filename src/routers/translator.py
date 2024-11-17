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

def translator_to_french(message: str) -> dict:
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
    return translator(message)


@router.post('/translator/')
async def chat(body: TranslatorToFrench):
    response = translator_to_french(body.message)
    return {'assistant': response}