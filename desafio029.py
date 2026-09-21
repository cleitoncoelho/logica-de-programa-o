numeros = []
n_impar = []
n_par = []

for i in range(1, 6):
    numero = int(input(f'Digite o número {i}: '))
    numeros.append(numero)
    if numero % 2 == 0:
        n_par.append(numero)
    else:
        n_impar.append(numero)

print('Pares:',n_par)
print('Ímpares:',n_impar)

# o gato correu muito rapido pela rua