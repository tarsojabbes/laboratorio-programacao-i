# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def encontra_menores(num, lista):
    for elemento in lista:
        if elemento < num:
            return elemento
    return -1