def verifica_par_impar(n):

    if n % 2 == 0:
        return f'{n} é par'
    else:
        return f'{n} é ímpar'

print(verifica_par_impar(4))
print(verifica_par_impar(7))