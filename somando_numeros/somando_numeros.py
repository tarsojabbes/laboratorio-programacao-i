# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220
# Calcula a soma dos ultimos numeros de uma sequência

quantidade_numeros = int(input())

soma = 0
numeros_inseridos = []

for i in range(quantidade_numeros):
    numero = int(input())

    numeros_inseridos.append(numero)
    soma += numero

media = soma/quantidade_numeros

soma_ultimos = 0

for i in range(len(numeros_inseridos) - 1, -1, -1):
    if numeros_inseridos[i] >= media:
        soma_ultimos += numeros_inseridos[i]
        break
    elif numeros_inseridos[i] < media:
        soma_ultimos += numeros_inseridos[i]
    

print(soma_ultimos)
