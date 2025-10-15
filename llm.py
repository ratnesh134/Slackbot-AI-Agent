from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq()

def chat(query: str):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": query}],
        model="openai/gpt-oss-120b"
    )

    return chat_completion.choices[0].message.content