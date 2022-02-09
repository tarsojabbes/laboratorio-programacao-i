# Computação - UFCG
# Programação 1
# Tarso Jabbes Lima de Oliveira

string = input()
horario = int(input())

if string != '':
    if horario >= 23 or horario <= 6:
        print("Perturbação Detectada!")
    else:
        print("Condomínio em Paz.")
else:
    print("Condomínio em Paz.")
