import openai
from config.settings import settings

openai.api_key = settings.OPENAI_API_KEY

def ask_gpt(history: list):
    """
    history = [(role, content), ...]
    """
    messages = [{"role": role, "content": text} for role, text in history]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message["content"]
