def eh_palindromo(palavra):
    return palavra == palavra[::-1]


def filtra_palindromos(lista):
    agrupado = []
    for palavra in lista:
        if eh_palindromo(palavra):
            agrupado.append(palavra)

    return agrupado


palavras = ['arara', 'python', 'ovo', 'casa', 'reviver']
print(filtra_palindromos(palavras))
