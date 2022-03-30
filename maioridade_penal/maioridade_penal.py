# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def maioridade_penal(string_nomes, string_idades):
    pessoas_maiores_idade = ''

    string_nomes = string_nomes.split()
    string_idades = string_idades.split()

    iterador = 0
    while iterador < len(string_nomes):
        if int(string_idades[iterador]) >= 18 and iterador != len(string_idades) - 1:
            pessoas_maiores_idade += string_nomes[iterador] + " "
        elif int(string_idades[iterador]) >= 18 and iterador == len(string_idades) - 1:
            pessoas_maiores_idade += string_nomes[iterador]
        iterador += 1

    return pessoas_maiores_idade
