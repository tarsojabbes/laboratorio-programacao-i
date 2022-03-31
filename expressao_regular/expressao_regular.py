# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def is_substring_expr(str1, str2):
    str2 = str2.split("*")

    letras_presentes = []
    i=0
    while i < len(str2):
        if str1[i] == str2[0][i]:
            letras_presentes.append(str1[i])
        i+=1
    
    presentes2 = []
    for j in range(len(str1)-1,len(str2[1]),-1):
        for k in range(len(str2[1])-1,-1,-1):
            if str1[j] == str2[1][k]:
                presentes2.append(str1[j])
                break

    if len(set(letras_presentes)) == len(str2[0]) and len(set(presentes2)) == len(str2[1]):
        return True
    return False
