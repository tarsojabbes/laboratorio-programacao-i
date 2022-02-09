# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

quantidade_reprovados = 0

while True:
    presenca_aluno = input()
    if presenca_aluno == "-":
        break

    iterador = 0
    faltas = 0
    while iterador < len(presenca_aluno):
        if presenca_aluno[iterador] == 'f':
            faltas += 1
        iterador += 1
    
    if faltas > 8:
        quantidade_reprovados += 1

print(f"{quantidade_reprovados} aluno(s) reprovado(s) por falta.")