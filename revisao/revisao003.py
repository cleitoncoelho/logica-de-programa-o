palavra = input('Digite uma palavra: ')

# eh_palindromo = True

for i in range(len(palavra) // 2):
    letra_inicio = palavra[i]
    letra_fim = palavra[len(palavra) - 1 - i]  # qual índice pega a letra "espelhada" de trás pra frente?
    
    if letra_inicio != letra_fim:
        eh_palindromo = False

# if eh_palindromo:
#     print(f'{palavra} é um palíndromo')
# else:
#     print(f'{palavra} não é um palíndromo')