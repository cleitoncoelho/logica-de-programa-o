def remove_duplicados(lista):
    unicos = set(lista)
    unicos_ordenados = sorted(unicos)
    return unicos_ordenados


print(remove_duplicados([4, 7, 4, 2, 7, 9, 2]))
