# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def calcula_conta(tabela):
    total = 0
    for i in range(1, len(tabela)):
        quantidade = 0
        tempo = 0
        watts = 0
        preco = 0
        for j in range(1, len(tabela[i])):
            if j == 1:
                quantidade += tabela[i][j]
            elif j == 2:
                tempo += tabela[i][j]
            elif j == 3:
                watts += tabela[i][j]
            preco += quantidade * watts * tempo * 0.28
        total += preco
    return f"R$ {total/1000:.2f}"
