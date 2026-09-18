palavra = input('Fi da peste, desgraçado. Digita uma palavra, por favor: ')

em_ordem = True

for i in range(len(palavra) - 1):
    if palavra[i] > palavra[i + 1]:
        em_ordem = False

if em_ordem:
    print(f'{palavra} está em ordem')
else:
    print(f'{palavra} não está em ordem')
