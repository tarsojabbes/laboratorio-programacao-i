# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

limite = int(input())

iterador = 1;

while iterador < limite:
    if iterador % 5 == 0 and iterador % 2 == 0:
        print(iterador)

    iterador += 1


