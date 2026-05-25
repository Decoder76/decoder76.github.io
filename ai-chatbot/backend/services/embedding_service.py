# Placeholder for lightweight semantic scoring.
def similarity_score(query: str, text: str) -> float:
    q_words = set(query.lower().split())
    t_words = set(text.lower().split())
    overlap = len(q_words & t_words)
    return overlap / max(len(q_words), 1)
