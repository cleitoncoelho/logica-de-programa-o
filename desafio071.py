def conta_letras(palavra):
    contagem = {}

    for letra in palavra.lower():
        contagem[letra] = contagem.get(letra, 0) + 1

    return contagem


print(conta_letras('bAnana'))
