from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_reply(messages):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # ✅ updated model
            messages=messages,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"