def saudacao_hora(nome, periodo='dia'):
    return f'Bom {periodo}, {nome}'


print(saudacao_hora('Carlos'))
print(saudacao_hora('Maria', 'noite'))
