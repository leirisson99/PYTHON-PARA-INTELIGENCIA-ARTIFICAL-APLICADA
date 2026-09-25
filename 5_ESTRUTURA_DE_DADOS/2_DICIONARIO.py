dict_de_nomes_e_medias = { "Ana": 8.5, "Bruno": 7.0, "Carla": 9.2, "Daniel": 6.5, "Eduarda": 8.0, "Felipe": 5.8, "Gabriel": 7.4 }

print(dict_de_nomes_e_medias["Daniel"])
print(dict_de_nomes_e_medias.get("Bruno"))

if not dict_de_nomes_e_medias.get("Leirisson"):
    print("Chave de valor não encontrado")
    print(dict_de_nomes_e_medias.get("Leirisson"))