# Guarda em snapshot uma cópia independente do historico antes de qualquer alteração.
# Escolhe a instrução conforme a nota:
# nota 1 ou 2 → "Identifique o problema principal e redija um pedido de desculpas."
# nota 3 → "Resuma os pontos positivos e negativos."
# nota 4 ou 5 → "Agradeça e destaque o elogio principal."
# Monta a mensagem do usuário (instrução + resenha) e adiciona ao historico com role igual a "user".
# Termina com print(len(historico), len(snapshot)), que deve imprimir 2 1.

# Desafio opcional: e se chegar nota = 7? Decida o que o código deve fazer e implemente.

mensagem_usuario = {"role":"user", "content": "você é um agente de suporte ao usuario e precisa avaliar os feedbacks deles e responder sempre com educação e clareza, queria saber onde encontro o meu pedido no site"}
resenha = "A entrega atrasou 10 dias e ninguém respondeu meu e-mail."
nota = 2
historico = [{"role": "system", "content": "Você é um analista de resenhas de e-commerce."}]
# realizando o snapshot do historico
backup_historico = historico.copy()

historico.append(mensagem_usuario)



if nota == 1 or nota == 2:
    historico.append({"role": "system", "content":"Desculpa estamos verificando o motivo do atraso do seu pedido."})
elif nota == 3:
    historico.append({"role": "system", "content": "ponto positivo o seu pedido já foi enviado, mas o negativo é que atrasou a entrega"})
elif nota == 4 or nota == 5:
    historico.append({"role": "system", "content": "O seu feddback é muito importante e obrigado pelo seu elogio."})
elif nota > 5:
    print("Obrigado pela avaliação")