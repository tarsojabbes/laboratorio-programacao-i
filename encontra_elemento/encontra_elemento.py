# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

numero_inteiro = int(input())
sequencia_inteiro = input().split()

presente_na_sequencia = False

for numero in sequencia_inteiro:
    if int(numero) == numero_inteiro:
        presente_na_sequencia = True

if presente_na_sequencia == True:
    print("sim")
else:
    print("não")
