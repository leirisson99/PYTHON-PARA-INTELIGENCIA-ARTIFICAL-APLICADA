from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("ERRO AO TENTAR BUSCAR A CHAVE DE API [🐞 | 👾 ]")

def main():
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(model="gemini-2.5-flash")
    while True:
        prompt = input("Digite a sua pergunta: ")
        if prompt.lower() == "sair":
            print("\nSaindo...")
            break
        resposta = chat.send_message(prompt)
        print(resposta.text)
        
        
    


if __name__ == "__main__":
    main()