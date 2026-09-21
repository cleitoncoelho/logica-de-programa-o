numeros = []

for i in range(1, 6):
    numero = int(input(f'Digite o número {i}: '))
    numeros.append(numero)

print(f'Lista original {numeros}')

menor_numero = min(numeros)
numeros.remove(menor_numero)

print(f'Lista após remover o menor: {numeros}')
