# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def matriz_menor(M1, M2):
    nova_matriz = [[], [], []]
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if M1[i][j] < M2[i][j]:
                nova_matriz[i].append(M1[i][j])
            else:
                nova_matriz[i].append(M2[i][j])
    return nova_matriz