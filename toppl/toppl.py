# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def filtra_alunos(alunos, inscritos, media_minima):
    numero_alunos = len(alunos)
    aptos = []
    for i in range(len(alunos)):
        esta_apto = False
        for j in range(len(inscritos)):
            if alunos[i][0] == inscritos[j] and alunos[i][1] >= media_minima:
                esta_apto = True
        
        if esta_apto:
            aptos.append(alunos[i])

    for i in range(len(alunos)):
        alunos.pop()

    for apto in aptos:
        alunos.append(apto)

    quantidade_remocoes = numero_alunos - len(alunos)

    return quantidade_remocoes
