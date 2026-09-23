def conta_vogais(frase):

    vogal = 0

    for letra in frase:
        if letra in 'aeiouáéíóú':
            vogal += 1
    return vogal


print(conta_vogais('python é legal'))
