# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def ordena_vpb(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista) - 1 - i):
            atual = lista[j]
            proximo = lista[j+1]
            if atual == "b" and proximo == "v":
                lista[j], lista[j+1] = lista[j+1],lista[j]
            if atual == "b" and proximo == "p":
                lista[j], lista[j+1] = lista[j+1],lista[j]
            if atual == "p" and proximo == "v":
                lista[j], lista[j+1] = lista[j+1],lista[j]