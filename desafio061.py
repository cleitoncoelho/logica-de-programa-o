def filtra_pares(lista):
    pares = [numero for numero in lista if numero % 2 == 0]
    return pares


print(filtra_pares([4, 7, 2, 9, 6, 3, 8]))
