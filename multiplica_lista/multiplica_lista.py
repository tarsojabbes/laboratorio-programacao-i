# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def multiplica_lista(n,lista):
    nova_lista = []

    while n != 0:
        for elemento in lista:
            nova_lista.append(elemento)
        n -= 1
    
    return nova_lista