def eh_par(numero):
    return numero % 2 == 0


def separa_par_impar(lista):
    agrupado = {}

    for numero in lista:
        if eh_par(numero):
            if 'pares' in agrupado:
                agrupado['pares'].append(numero)
            else:
                agrupado['pares'] = [numero]
        else:
            if 'impares' in agrupado:
                agrupado['impares'].append(numero)
            else:
                agrupado['impares'] = [numero]

    return agrupado


numeros = [4, 7, 2, 9, 6, 3]
print(separa_par_impar(numeros))
