quantidade = int(input('Quantos numeros você vai digitar? '))

numero = int(input('Digite um número: '))
maior = menor = numero

for i in range(quantidade - 1):
    numero = int(input('Digite um número: '))

    if numero > maior:  # noqa: PLR1730
        maior = numero

    if numero < menor:  # noqa: PLR1730
        menor = numero


print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
