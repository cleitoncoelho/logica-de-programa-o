numero = int(input('Digite um número: '))

eh_primo = True

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False

    if not eh_primo:
        print(f'O número {numero} não é primo')
    else:
        print(f'O número {numero} é primo')

else:
    print(f'{numero} não é primo')
