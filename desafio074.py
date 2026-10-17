def tres_maiores_palavras(lista):
    lista_ordenada = sorted(lista, key=len, reverse=True)
    maiores_palavras = lista_ordenada[:3]
    return maiores_palavras


print(tres_maiores_palavras(['python', 'sol', 'casa', 'computador', 'rio', 'elefante']))
