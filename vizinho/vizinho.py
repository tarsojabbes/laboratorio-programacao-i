# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

sequencia = input().split()

mesmo_valor = 0

for i in range(1, len(sequencia)):
    if sequencia[i - 1] == sequencia[i]:
        mesmo_valor += 1

print(mesmo_valor)
