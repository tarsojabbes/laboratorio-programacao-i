# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def flipmove(lista, k):
    for i in range(k - 1, -1, -1):
        lista.append(lista[i])
        lista.pop(i)

    return lista
