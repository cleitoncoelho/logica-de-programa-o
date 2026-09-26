def agrupar_por_par_impar(lista):
    agrupado = {}

    for numero in lista:
        if numero % 2 == 0:
            if 'par' in agrupado:
                agrupado['par'].append(numero)
            else:
                agrupado['par'] = [numero]
        else:
            if 'impar' in agrupado:
                agrupado['impar'].append(numero)
            else:
                agrupado['impar'] = [numero]

    return agrupado


numeros = [4, 7, 2, 9, 6, 3]
print(agrupar_por_par_impar(numeros))
