# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

numero1 = float(input())
numero2 = float(input())
numero3 = float(input())

numeros_iguais = 0;

if numero1 == numero2:
    numeros_iguais += 1
if numero1 == numero3:
    numeros_iguais += 1
if numero2 == numero3:
    numeros_iguais += 1

if numeros_iguais == 1:
    numeros_iguais += 1

print(numeros_iguais)
