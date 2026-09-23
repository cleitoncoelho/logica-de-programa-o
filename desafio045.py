def analisar_numeros(lista):
    # dados = {}

    # maior = max(lista)
    # dados['maior'] = maior

    # menor = min(lista)
    # dados['menor'] = menor

    # media = sum(lista) / len(lista)
    # dados['media'] = media

    # quantidade = len(lista)
    # dados['quantidade'] = quantidade

    # return dados

    return {
        'maior': max(lista),
        'menor': min(lista),
        'media': sum(lista) / len(lista),
        'quantidade': len(lista),
    }


numeros = [10, 20, 30, 40]
print(analisar_numeros(numeros))
