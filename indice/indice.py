# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def indice_remissivo(texto):
    texto = texto.split()

    indice = {}
    for palavra in texto:
        indices = []
        vezes = meu_in(texto, palavra)
        indice[palavra] = acha_indice(texto, palavra)

    return indice

def acha_indice(lista, termo):
    indices = []
    for i in range(len(lista)):
        if lista[i] == termo:
            indices.append(i)
    return indices

def meu_in(lista, termo):
    vezes = 0
    for elem in lista:
        if elem == termo:
            vezes+=1
    return vezes
