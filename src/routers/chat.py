from src.models.chat import AutoCompleteModel
from fastapi import APIRouter
from transformers import pipeline

router = APIRouter()


def generate_response(message: str) -> dict:
    generator = pipeline('text-generation',model='gpt2')
    return generator(message)

@router.post('/autocomplete/')
async def chat(body: AutoCompleteModel):
    response = generate_response(body.message)
    return {'assistant': response}