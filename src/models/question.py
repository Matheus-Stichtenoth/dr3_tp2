from pydantic import BaseModel

class QuestionFixed(BaseModel):
    question: str