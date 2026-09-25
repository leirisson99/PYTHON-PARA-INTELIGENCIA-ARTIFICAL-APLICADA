from google import genai
from google.genai import errors
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada. Verifique o arquivo .env")
    
     
client = genai.Client(api_key=API_KEY)

# O chat guarda o histórico da conversa entre as perguntas
chat  = client.chats.create(model="gemini-2.5-flash")

def chamando_agent(question: str) -> str:
    try:
        for chunk in chat.send_message_stream(question):
            print(chunk.text or "", end="", flush=True)
        print()
        
    except errors.ServerError as e:
        print(f"Servidor do Gemini indisponível ({e.code}). Tente novamente mais tarde.")
    except errors.ClientError as e:
        print(f"Erro na requisição ({e.code}): {e.message}")
        
if __name__=="__main__":
    print("SISTEMA COM AGENTE GOOGLE (digite 'sair' para encerrar)")
    while True:
        question = input("\nO que você está pensando ?\n")
        if question.lower() == "sair":
            break
        print("Gemini: \n", end="")
        chamando_agent(question)
