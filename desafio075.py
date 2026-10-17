def eh_anagrama(a, b):

    anagrama = False

    palavra_1 = sorted(a)
    palavra_2 = sorted(b)

    if palavra_1 == palavra_2:
        anagrama = True

    return anagrama


print(eh_anagrama('casa', 'cas'))

