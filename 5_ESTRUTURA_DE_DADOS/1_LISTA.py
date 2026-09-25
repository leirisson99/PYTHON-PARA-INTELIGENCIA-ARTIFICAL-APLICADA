

# lista_de_nome = [
#     "Leirisson",
#     "Souza",
#     "dos",
#     "santos"
# ]


# for nome in lista_de_nome:
#     print(nome)


contador = 0
lista_de_medias = [7.5, 8.0, 6.2, 9.5, 5.8, 7.0, 8.4]

while  True:
    lista_de_medias[contador] += 1
    
    if lista_de_medias[contador] >= 10:
        break
    
    print(lista_de_medias[contador])
    
    contador+=1