def classificar_alunos(alunos, nota_corte):
    aprovados = []
    reprovados = []
    soma_notas = 0
    
    for aluno in alunos:
        soma_notas += aluno['nota']
        if aluno['nota'] >= nota_corte:
            aprovados.append(aluno['nome'])
        else:
            reprovados.append(aluno['nome'])

    media = soma_notas / len(alunos)
    return {
        'aprovados': aprovados,
        'reprovados': reprovados,
        'media_turma': media
    }

turma = [
    {'nome': 'Ana', 'nota': 8.5},
    {'nome': 'Bruno', 'nota': 5.0},
    {'nome': 'Carla', 'nota': 7.0},
    {'nome': 'Diego', 'nota': 4.5}
]
print(classificar_alunos(turma, 6.0))