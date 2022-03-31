# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

tabela = {"H": 1, "S": 32, "O": 16, "C": 12, "Ca": 40, "Na": 23, "P": 31}
while True:
    formula = input()

    if formula == "fim":
        break

    formula = formula.split()

    massa = 0

    for i in range(len(formula)):
        if not formula[i].isdigit():
            if i != len(formula)-1 and formula[i+1].isdigit():
                massa += tabela[formula[i]] * int(formula[i+1])
            else:
                massa += tabela[formula[i]]
    print(massa)

