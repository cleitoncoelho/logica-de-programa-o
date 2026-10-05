def pede_idade_valida():
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            if idade >= 0:
                return idade
            else:
                print('Não existe idade negativa')

        except ValueError:
            print('Digite apenas números.')


print(pede_idade_valida())
