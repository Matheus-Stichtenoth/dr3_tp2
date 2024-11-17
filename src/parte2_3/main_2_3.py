from fastapi import FastAPI
from src.routers.translator_germany import router as translator_router

app = FastAPI()

app.include_router(translator_router, prefix='/chat')

@app.get('/')
async def root():
    return {'message':'Hello World'}