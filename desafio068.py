def soma_valores_validos(lista):
    soma = 0
    for numero in lista:
        try:
            numero_int = int(numero)
            soma += numero_int
        except ValueError:
            continue
    return soma


valores = ['20', 'abc', '5', 'xyz','10']
print(soma_valores_validos(valores))
