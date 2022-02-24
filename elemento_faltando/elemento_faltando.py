# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def elemento_faltando(lista1, lista2):
    soma_lista1 = 0
    for elemento in lista1:
        soma_lista1 += elemento
    
    soma_lista2 = 0
    for elemento in lista2:
        soma_lista2 += elemento

    elemento_faltando = abs(soma_lista1-soma_lista2)
    
    return elemento_faltando
