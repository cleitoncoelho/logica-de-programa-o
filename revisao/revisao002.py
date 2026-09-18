numero = int(input('Digite um numero: '))

soma = 0
for i in range(2, numero + 1, 2):
    soma += i

print(f'A soma dos pares até {numero} é {soma}')

