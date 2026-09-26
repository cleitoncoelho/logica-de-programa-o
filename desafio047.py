def resumo_compras(produtos, orcamento):
    produtos_caros = []
    soma_produtos = 0
    dentro_orcamento = True

    for produto in produtos:
        soma_produtos += produto['preco']

        if soma_produtos > orcamento:
            dentro_orcamento = False

        if produto['preco'] > 50:
            produtos_caros.append(produto['nome'])

    return {
        'total': soma_produtos,
        'dentro_orcamento': dentro_orcamento,
        'produtos_caros': produtos_caros,
    }


produtos = [
    {'nome': 'Mouse', 'preco': 45.0},
    {'nome': 'Teclado', 'preco': 90.0},
    {'nome': 'Monitor', 'preco': 600.0},
]

print(resumo_compras(produtos, 500))
