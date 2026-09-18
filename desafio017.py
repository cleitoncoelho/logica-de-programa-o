frase = input('Digite uma frase: ')  
palavras = frase.split()

maior_palavra = palavras[0]
for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra


print(f'A maior palavra é {maior_palavra}')
