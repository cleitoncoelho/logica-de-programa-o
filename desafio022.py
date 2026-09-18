numeros = []
soma = 0

for i in range(1, 6):
    numero = int(input(f'Digite o número {i}: '))
    soma += numero
    numeros.append(numero)

media = soma / 5

contador = 0

for n in numeros:
    if n > media:
        contador += 1

print(f'A média é {media}')
print(f'{contador} são maiores que a média')
