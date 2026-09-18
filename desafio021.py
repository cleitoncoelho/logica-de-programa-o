todos_positivos = True


for i in range(1, 6):
    numero = int(input(f'Digite o {i}° numero: '))

    if numero <= 0:
        todos_positivos = False


if todos_positivos:
    print('Todos os números digitados são positivos')
else:
    print('Foi digitado número negativo')
