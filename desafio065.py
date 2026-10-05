def converte_numero(txt):
    try:
        return int(txt)
    except ValueError:
        return 'Valor inválido'

print(converte_numero('42'))
print(converte_numero('abc'))