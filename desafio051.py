def eh_par(numero):
    return numero % 2 == 0


def conta_pares(lista):
    contador = 0
    for numero in lista:
        if eh_par(numero):
            contador += 1

    return contador


numeros = [4, 7, 2, 9, 6, 3]
print(conta_pares(numeros))
