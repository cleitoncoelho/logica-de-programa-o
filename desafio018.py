palavra = input('Digite uma palavra: ').lower()

contador = 0

for letra in palavra:
    if 'a' in letra:
        contador += 1

if contador > 1:
    print(f'A letra "a" aparece {contador} vezes')
elif contador == 1:
    print(f'A letra "a" aparece {contador} vez')
else:
    print('A letra "a" não aparece na palavra')
