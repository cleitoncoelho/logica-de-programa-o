def formata_nome(nome, maiuscula=False):
    if maiuscula:
        return nome.upper()
    return nome.capitalize()


print(formata_nome('joão', True))
