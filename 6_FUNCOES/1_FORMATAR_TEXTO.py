


def formatar_texto(texto: str) -> str:
    return texto.strip().upper()


if __name__ == "__main__":
    texto2 = "   aNa cArLa  sILvA   "
    texto3 = "bRuNo  mARqUeS   oLIvEiRa"
    texto4 = "   cARLOS   eDuArDo   sANtoS "
    texto5 = "dANieLA   fERnAnDeS    cRUZ "
    texto6 = "   eDuArDo  hEnRiQuE   lImA"
    
    print(formatar_texto(texto = texto2))