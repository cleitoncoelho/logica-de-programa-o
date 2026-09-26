def agrupar_por_tamanho(lista):
    agrupado = {}

    for palavra in lista:

        if len(palavra) in agrupado:
            agrupado[len(palavra)].append(palavra)
        else:
            agrupado[len(palavra)] = [palavra]

    return agrupado

palavras = ['sol', 'lua', 'python', 'casa', 'rio']
print(agrupar_por_tamanho(palavras))