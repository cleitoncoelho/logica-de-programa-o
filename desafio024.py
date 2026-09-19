numeros = []

for i in range(1, 6):
    numero = int(input(f'Digite o número {i}: '))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print(f'A soma é {soma}')
print(f'A média é {media}')
