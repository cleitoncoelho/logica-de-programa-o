def ordena_por_tamanho_desc(lista):
    return sorted(lista, key=len, reverse=True)
    


print(ordena_por_tamanho_desc(['python', 'sol', 'casa', 'computador', 'rio']))
