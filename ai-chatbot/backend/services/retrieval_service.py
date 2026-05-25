import json
from pathlib import Path

KB_PATH = Path(__file__).resolve().parents[1] / 'knowledge' / 'chatbot_knowledge.json'

def retrieve_context(question: str):
    data = json.loads(KB_PATH.read_text())
    q = question.lower()
    if 'project' in q:
        return data.get('projects', [])
    if 'skill' in q or 'technology' in q:
        return data.get('skills', [])
    if 'experience' in q or 'ml' in q:
        return data.get('experience', [])
    return [data.get('about', '')]
