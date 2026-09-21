frase = input('Digite uma frase: ')
palavras = frase.split()

palavra_maior_4 = []

for palavra in palavras:
    if len(palavra) > 4:
        palavra_maior_4.append(palavra)

print('Palavras com mais de 4 letras:',palavra_maior_4)