numero = int(input('Digite um número: '))
numero_str = str(numero)
numero_invertido = numero_str[::-1]

if numero_str == numero_invertido:
    print(f'{numero} é um número palíndromo')
else:
    print(f'{numero} não é um número palíndromo')
