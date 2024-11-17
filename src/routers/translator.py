from src.models.translator import TranslatorToFrench
from fastapi import APIRouter
from transformers import pipeline

router = APIRouter()

def translator_to_french(message: str) -> dict:
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
    return translator(message)

@router.post('/translator/')
async def chat(body: TranslatorToFrench):
    response = translator_to_french(body.message)
    return {'assistant': response}