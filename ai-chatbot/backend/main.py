from fastapi import FastAPI
from pydantic import BaseModel
from services.retrieval_service import retrieve_context
from services.response_builder import build_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Recruiter Portfolio Chatbot")

class ChatRequest(BaseModel):
    question: str

@app.post('/chat')
def chat(req: ChatRequest):
    context = retrieve_context(req.question)
    return {"answer": build_response(req.question, context)}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://decoder76.github.io",
        "http://localhost:4000",
        "http://127.0.0.1:4000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
