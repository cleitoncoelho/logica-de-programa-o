numeros = {}


for i in range(1, 6):
    eh_primo = True
    numero = int(input(f'Digite o número {i}: '))

    for n in range(2, numero):
        if numero % n == 0:
            eh_primo = False

    if not eh_primo:
        numeros[numero] = 'não primo'
    else:
        numeros[numero] = 'primo'

print(numeros)
