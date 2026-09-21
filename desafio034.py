palavras = {}

for i in range(1, 6):
    palavra = input(f'Digite a palavra {i}: ')

    palavras[palavra] = len(palavra)

print(palavras)
