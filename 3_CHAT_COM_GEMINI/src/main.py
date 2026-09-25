from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("Erro ao tentar ler API KEY do GEMINI 😒")



def main():
    client = genai.Client(api_key=API_KEY)
    
    question = input("Em que você está pensando ?: ")
    chat = client.chats.create(model="gemini-2.5-flash")
    respostaLLM = chat.send_message(question)
    textoResposta = respostaLLM.text
    print(textoResposta)
   
if __name__=="__main__":
    main()