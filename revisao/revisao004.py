palavra = input('Digite uma palavra: ')  # entrada de dados

eh_palindromo = True  # flag (ponto de inicio)

for i in range(len(palavra) // 2):  # for para percorrer as letras | "//" para dividir a palavra na metade
    letra_inicio = palavra[i]  # letra inicio sera o primeiro indice da palavra
    letra_fim = palavra[len(palavra) - 1 - i]  # letra fim sera a letra no indice negativo, "- i" farar a letra atualizar a cada loop

    if letra_inicio != letra_fim: # compara as letras inicias e finais
        eh_palindromo = False # caso as letras sejam diferentes a flag atualiza para False

if eh_palindromo: # se forem iguais... 
    print(f'{palavra} é palíndromo')
else: # se forem diferentes...
    print(f'{palavra} não é palíndromo')
