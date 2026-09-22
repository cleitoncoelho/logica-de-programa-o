palavras = {}

for i in range (1, 6):
    palavra = input(f'Digite a palavra {i}: ')

    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        palavras[palavra] = 'é palíndromo'
    else:
        palavras[palavra] = 'não é palíndromo'

print(palavras)