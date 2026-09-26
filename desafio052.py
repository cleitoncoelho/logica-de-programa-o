def eh_primo(numero):
    primo = True

    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                primo = False

        return primo
    else:
        return False


def filtra_primos(lista):
    agrupado = []

    for numero in lista:
        if eh_primo(numero):
            agrupado.append(numero)

    return agrupado


numeros = [4, 7, 8, 11, 9, 13, 6]
print(filtra_primos(numeros))
