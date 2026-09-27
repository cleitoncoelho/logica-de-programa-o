def conta_vogal(palavra):
    vogal = 0
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            vogal += 1
    return vogal


def maior_quantidade_vogais(lista):
    maior_palavra = lista[0]

    for palavra in lista:
        if conta_vogal(palavra) > conta_vogal(maior_palavra):
            maior_palavra = palavra

    return maior_palavra


palavras = ['banana', 'uva', 'melancia', 'kiwi']
print(maior_quantidade_vogais(palavras))
