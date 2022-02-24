# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def elimina_kyw(frase):
    nova_frase = ''

    for elemento in frase:
        if elemento == 'k' or elemento == 'y' or elemento == 'w':
            continue
        else:
            nova_frase += elemento
    
    return nova_frase