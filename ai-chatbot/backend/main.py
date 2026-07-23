from fastapi import FastAPI
from pydantic import BaseModel
from services.retrieval_service import retrieve_context
from services.response_builder import build_response

app = FastAPI(title="Recruiter Portfolio Chatbot")

class ChatRequest(BaseModel):
    question: str

@app.post('/chat')
def chat(req: ChatRequest):
    context = retrieve_context(req.question)
    return {"answer": build_response(req.question, context)}
