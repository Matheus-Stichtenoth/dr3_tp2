from fastapi import FastAPI
from src.routers.question import router as router_question

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Inclui o roteador
app.include_router(router_question, prefix="/chat", tags=["Questions"])

@app.get('/')
async def root():
    return {'message':'Hello World'}
