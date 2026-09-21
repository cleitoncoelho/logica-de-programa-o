frase = input('Digite uma frase: ').lower()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

eh_pangrama = True

for letra in alfabeto:
    if letra not in frase:
        eh_pangrama = False

if eh_pangrama:
    print('É um pangrama')
else:
    print('Não é um pangrama')
