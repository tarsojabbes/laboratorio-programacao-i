# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def agrupa_pares_impares(seq):
    for i in range(len(seq) -1):
        for j in range(len(seq)-1-i):
            e_par = seq[j]%2==0
            proximo_e_par = seq[j+1]%2==0
            if not e_par and proximo_e_par:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    
    return seq