def tamanhos_palavras(lista):
    tamanho = [len(palavra) for palavra in lista]
    return tamanho


print(tamanhos_palavras(['casa', 'sol', 'python']))
