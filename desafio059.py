def processa_pedidos(lista, taxa_extra=0):
    produtos_caros = []
    soma_produtos = 0

    for produto in lista:
        soma_com_taxa = produto['valor'] + (produto['valor'] * taxa_extra / 100)
        soma_produtos += soma_com_taxa

        if soma_com_taxa > 100:
            produtos_caros.append(produto['produto'])

    return {'total': soma_produtos, 'pedidos_caros': produtos_caros}


pedidos = [
    {'produto': 'Livro', 'valor': 40},
    {'produto': 'Fone', 'valor': 90},
    {'produto': 'Notebook', 'valor': 2000},
]

print(processa_pedidos(pedidos,20))
