numeros = {}

for i in range(1, 6):
    numero = int(input(f'Digite o numero {i}: '))

    if numero % 2 == 0:
        numeros[numero] = 'par'
    else:
        numeros[numero] = 'impar'

print(numeros)
