# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def remove_duplas(lista):
    nova_lista = []
    for i in range(len(lista)):
        qtd = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                qtd += 1
        if qtd != 2:
            nova_lista.append(lista[i])

    for k in range(len(lista)):
        lista.pop()
    for l in range(len(nova_lista)):
        lista.append(nova_lista[l])
