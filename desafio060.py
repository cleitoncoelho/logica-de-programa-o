def estatisticas_lista(lista):
    return sum(lista), sum(lista) / len(lista), len(lista)

soma, media, qtd = estatisticas_lista([10, 20, 30, 40])
print(soma, media, qtd)