def agrupar_por_categoria(lista):
    agrupado = {}

    for produto in lista:
        categoria = produto['categoria']
        nome = produto['nome']

        if categoria in agrupado:
            agrupado[categoria].append(nome)
        else:
            agrupado[categoria] = [nome]

    return agrupado
        
produtos = [
    {'nome': 'Mouse', 'categoria': 'Periférico'},
    {'nome': 'Teclado', 'categoria': 'Periférico'},
    {'nome': 'Monitor', 'categoria': 'Tela'},
]

print(agrupar_por_categoria(produtos))