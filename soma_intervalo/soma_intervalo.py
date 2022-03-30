# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def soma_intervalo(numero_inicial, numero_final):
    soma = 0
    numero = numero_inicial
    for i in range(numero_inicial, numero_final+1):
        soma += numero
        numero += 1
    
    return soma