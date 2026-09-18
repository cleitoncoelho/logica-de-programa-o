palavra = input('Fi da peste, desgraçado. Digita uma palavra, por favor: ').strip().lower()

contador = 0

for letra in palavra:
    if letra not in 'aeiouáéíóú':
        contador += 1

if contador > 1:
    print(f'A palavra tem {contador} consoantes')
elif contador == 1:
    print(f'A palavra tem {contador} consoante')
else:
    print('A palavra não tem consoantes')