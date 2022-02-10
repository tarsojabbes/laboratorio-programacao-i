# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

quantidade_numeros = int(input())

soma_numeros_pares = 0
quantidade_numeros_pares = 0

numeros_inseridos = []
numeros_pares = []

for i in range(quantidade_numeros):
    numero = int(input())
    numeros_inseridos.append(numero)

    if numero % 2 == 0:
        numeros_pares.append(numero)
        quantidade_numeros_pares += 1
        soma_numeros_pares += numero

media = soma_numeros_pares/quantidade_numeros_pares

quantidade_acima_media = 0

for numero in numeros_inseridos:
    if numero > media:
        quantidade_acima_media += 1

print(f"média dos pares: {media:.1f}")
print(f"acima da média: {quantidade_acima_media}")



