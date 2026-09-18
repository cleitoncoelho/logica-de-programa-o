frase = input('Digite uma frase: ').lower()

vogal = 0
for letra in frase:
    if letra in 'aeiouáéíóú':
        vogal += 1

print(f'A frase tem {vogal} vogais')
