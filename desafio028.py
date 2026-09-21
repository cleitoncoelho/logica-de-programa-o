numeros = []

for i in range(1, 6):
    numero = int(input(f'Digite o numero {i}: '))
    numeros.append(numero)

numeros.sort()
print(f'Lista ordenada: {numeros}')
