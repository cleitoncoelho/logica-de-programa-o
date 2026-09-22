vogais = {} # DICIONARIO
frase = input('Digite uma frase: ')

for letra in frase: # letra == chave
    if letra in 'aeiouáéíóú':
        if letra in vogais:
            vogais[letra] += 1
        else:
            vogais[letra] = 1


print(vogais)