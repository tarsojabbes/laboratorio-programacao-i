# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())

if numero4 >= numero3:
    numero4, numero3 = numero3, numero4
if numero3 >= numero2:
    numero3, numero2 = numero2, numero3
if numero2 >= numero1:
    numero2, numero1 = numero1, numero2


print(numero1, numero2, numero3, numero4)