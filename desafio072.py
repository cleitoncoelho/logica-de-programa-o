def ordena_por_tamanho(lista):
    return sorted(lista, key=len)


print(ordena_por_tamanho(['python', 'sol', 'casa', 'computador', 'rio']))
