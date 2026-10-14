def ordena_por_tamanho(lista):
    lista_ordenada = sorted(lista, key=len)
    return lista_ordenada


print(ordena_por_tamanho(['python', 'sol', 'casa', 'computador', 'rio']))
