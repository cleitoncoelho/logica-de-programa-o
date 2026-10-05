def pede_numero_valido():
    while True:
        try:
            numero = int(input('Digite um numero: '))
            return numero
        except ValueError:
            print('Isso não é um número válido, tente de novo.')

print(pede_numero_valido())