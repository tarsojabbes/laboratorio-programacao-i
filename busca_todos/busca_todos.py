# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def busca_matriz(m, e):
    lista_ocorrencias = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == e:
                tupla_indices = (i,j)
                lista_ocorrencias.append(tupla_indices)
    return lista_ocorrencias