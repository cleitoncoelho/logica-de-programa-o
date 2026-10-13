def remove_duplicados(lista):
    unicos = []

    for numero in lista:
        if numero not in unicos:
            unicos.append(numero)

    return unicos


print(remove_duplicados([4, 7, 4, 2, 7, 9, 2]))
