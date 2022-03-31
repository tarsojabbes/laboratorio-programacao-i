# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def diagonais(M):
    matriz_diagonais = [[],[]]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i == j:
                matriz_diagonais[0].append(M[i][j])
        for k in range(len(M[i])):
            matriz_diagonais[1].append(M[i][j - i])
            break
    return matriz_diagonais