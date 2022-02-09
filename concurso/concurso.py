# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

# Coleta de dados do primeiro candidato
escrita_c1 = float(input())
didatica_c1 = float(input())
titulacao_c1 = float(input())
idade_c1 = int(input())

# Coleta de dados do segundo semestre
escrita_c2 = float(input())
didatica_c2 = float(input())
titulacao_c2 = float(input())
idade_c2 = int(input())

# Calculo de nota primeiro candidato
nota_c1 = (escrita_c1 * 0.3) + (didatica_c1 * 0.4) + (titulacao_c1 * 0.3)

# Cálculo de nota do segundo candidato
nota_c2 = (escrita_c2 * 0.3) + (didatica_c2 * 0.4) + (titulacao_c2 * 0.3)

if nota_c1 > nota_c2:
    print(f"O primeiro candidato foi aprovado com média {nota_c1:.1f}.")
elif nota_c2 > nota_c1:
    print(f"O segundo candidato foi aprovado com média {nota_c2:.1f}.")
else:
    if idade_c1 > idade_c2:
        print(f"O primeiro candidato foi aprovado com média {nota_c1:.1f}.")
    elif idade_c2 > idade_c1:
        print(f"O segundo candidato foi aprovado com média {nota_c2:.1f}.")
    else:
        print(f"Empate.")
