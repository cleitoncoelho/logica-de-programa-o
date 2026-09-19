numeros = []

for i in range(1, 6):
    numero = int(input(f'Digite o número {i}: '))
    numeros.append(numero)

numero_na_lista = int(input('Digite um número para buscar: '))

if numero_na_lista in numeros:
    print(f'O número {numero_na_lista} está na lista')
else:
    print(f'O número {numero_na_lista} não está na lista')
