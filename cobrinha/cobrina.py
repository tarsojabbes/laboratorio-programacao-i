# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def cobrinha(M):
    lista_impares = []
    for i in range(len(M)):
        if i%2 == 0:
            for j in range(len(M[i])):
                if M[i][j]%2 != 0:
                    lista_impares.append(M[i][j])
        else:
            for k in range(len(M[i])-1, -1, -1):
                if M[i][k]%2 != 0:
                    lista_impares.append(M[i][k])
    return lista_impares
