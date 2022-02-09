# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

numero = int(input())

if numero == 1:
    print(1)
else:
    for i in range(1, numero):
        if numero%i == 0:
            print(i)

