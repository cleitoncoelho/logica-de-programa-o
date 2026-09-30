def maiusculas_longas(lista):
    resultado = [palavra.upper() for palavra in lista if len(palavra) > 4]
    return resultado


print(maiusculas_longas(['sol', 'python', 'casa', 'computador']))
