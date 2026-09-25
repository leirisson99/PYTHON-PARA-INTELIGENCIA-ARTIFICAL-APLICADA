from google import genai
from google.genai import errors
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada. Verifique o arquivo .env")
    
     
client = genai.Client(api_key=API_KEY)

question = input("O que você está pensando ?:  ")

try:
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    print(resposta.text)
    
except errors.ServerError as e:
     print(f"Servidor do Gemini indisponível ({e.code}). Tente novamente mais tarde.")
except errors.ClientError as e:
    print(f"Erro na requisição ({e.code}): {e.message}")