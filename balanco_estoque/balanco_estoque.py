# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def balanco(d1, d2):
    d3 = {}
    for valor in d1:
        d3[valor] = d1[valor]
    for valor in d2:
        if d3.get(valor) == None:
            d3[valor] = d2[valor]
        else:
            d3[valor] += d2[valor]
    return d3


