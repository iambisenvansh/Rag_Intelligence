SYSTEM_PROMPT = """
You are a professional document analysis assistant.

Rules:
- Answer ONLY from the given context
- Be concise and structured
- If asked about experience, summarize clearly
- Use bullet points when possible
- Do NOT repeat raw document text
"""

def build_prompt(context: str, question: str) -> str:
    return f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer in clear bullet points:
"""
