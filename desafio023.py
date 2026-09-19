numeros = []

for i in range(1, 6):
    numero = int(input(f'Digite o número {i}: '))
    numeros.append(numero)

numeros_invertidos = numeros[::-1]


numeros_texto = []

for n in numeros_invertidos:
    numeros_texto.append(str(n))

resultado = ', '.join(numeros_texto)


print(f'Ordem inversa: {resultado}')
