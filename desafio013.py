soma = 0
for i in range(1, 6):
    numero = float(input(f'Digite o {i}° numero: '))
    soma += numero

media = soma / 5
print(f'A média é {media}')
