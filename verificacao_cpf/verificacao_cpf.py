# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def calcula_digitos_verificacao(cpf):
    cpf = list(cpf)

    cpf_inteiros = []
    for numero in cpf:
        cpf_inteiros.append(int(numero))

    somatorio_primeiro_digito = somatorio_digitos(cpf_inteiros)
    primeiro_digito = (somatorio_primeiro_digito*10)%11

    if primeiro_digito == 10:
        primeiro_digito = 0
    
    cpf_inteiros.append(primeiro_digito)
    somatorio_segundo_digito = somatorio_digitos(cpf_inteiros)
    segundo_digito = (somatorio_segundo_digito*10)%11

    if segundo_digito == 10:
        segundo_digito = 0

    return f"{primeiro_digito}{segundo_digito}"
    

def somatorio_digitos(cpf_inteiros):
    somatorio = 0
    multiplicador = 2
    for i in range(len(cpf_inteiros)-1, -1,-1):
        valor = cpf_inteiros[i] * multiplicador
        somatorio += valor
        multiplicador += 1
    
    return somatorio
