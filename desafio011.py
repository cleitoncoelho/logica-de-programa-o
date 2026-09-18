numero = int(input('Digite um numero: '))

anterior = 0
atual = 1

if numero >= 2:
    print(anterior, end=', ')
    print(atual, end=', ')

    for i in range(numero - 2):
        proximo = anterior + atual
        print(proximo, end=', ')

        anterior = atual
        atual = proximo

elif numero == 1:
    print(anterior)
else:
    print('Nenhum termo foi digitado')
