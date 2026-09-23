def filtrar_maiores_que_media(lista):

    media = sum(lista) / len(lista)

    maior_media = []
    for n in lista:
        if n > media:
            maior_media.append(n)

    return maior_media


numeros = [-10, 0, 10, 20]

print(filtrar_maiores_que_media(numeros))
