# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220
# Prova de Reposição | Data: 30 de Março de 2022

# Resumo: um programa que recebe uma sequência de números
# inteiros e classifica-a em válida ou inválida. Será válida se
# a quantidade de número pares for mais que a de ímpares.

# Entrada do programa: sequência de números inteiros
# Saída do programa: uma linha que indica se a sequência é válida ou não
# seguida da própria sequência
# Condição de parada: quando a entrada do programa for "fim"

# Ao fim do programa, uma linha deve ser impressa indicando
# as linhas inválidas lidas e a quantidade de sequências inválidas

sequencias_lidas = 0
sequencias_invalidas = 0
while True:
    sequencia = input()

    if sequencia == "fim":
        break

    sequencia = sequencia.split()
    sequencias_lidas += 1

    quantidade_pares = 0
    quantidade_impares = 0
    for numero in sequencia:
        numero_inteiro = int(numero)
        if (numero_inteiro%2==0):
            quantidade_pares += 1
        else:
            quantidade_impares += 1
    
    if quantidade_impares > quantidade_pares:
        print(f"linha {sequencias_lidas} inválida: ", end="")
        for i in range(len(sequencia)):
            if (i != len(sequencia) - 1):
                print(f"{sequencia[i]} ", end="")
            else:
                print(f"{sequencia[i]}")
        sequencias_invalidas += 1

print(f"sequências lidas: {sequencias_lidas} (inválidas: {sequencias_invalidas})")
    