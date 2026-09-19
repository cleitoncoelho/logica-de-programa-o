numeros = []

for i in range(1, 6):
    numero = int(input(f'Digite o número {i} : '))
    numeros.append(numero)

numero_na_lista = int(input('Digite um número para buscar: '))

qtd_numero_lista = 0

for n in numeros:
    if n == numero_na_lista:
        qtd_numero_lista += 1
    
if qtd_numero_lista > 1:
    print(f'O número {numero_na_lista} aparece {qtd_numero_lista} vezes na lista')
elif qtd_numero_lista == 1:
    print(f'O número {numero_na_lista} aparece {qtd_numero_lista} vez na lista')
else:
    print(f'O número {numero_na_lista} não está na lista')


    