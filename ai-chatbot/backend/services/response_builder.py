def build_response(question: str, context):
    return f"Based on your question: '{question}', here are relevant highlights: {', '.join(context)}"
