# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220
# Prova 2 | Data: 21 de Março de 2022

# Resumo: um programa que ofusca uma linha pelas seguintes regras:
# 1) Troca letras maiúsculas por minúsculas e vice-versa
# 2) Troca algumas letras por números e vice-versa seguindo o mapa:
#       Letra A ou a - 4 Letra B ou b - 8 Letra E ou e - 3 
#       Letra G ou g - 6 Letra I ou i - 1 Letra L ou l - 7 
#       Letra S ou s - 5 Letra O ou o - 0
# 3) Troca k espaços por "*" onde k é o tamanho da palavra anterior

# Parâmetro da função: uma string
# Retorno da função: a mesma string depois de processada pelo ofuscador

def ofuscador(linha):
    codigo_ofuscado = ""

    for i in range(len(linha)):
        if not linha[i].isdigit() and not linha[i] == " ":
            if 65 <= ord(linha[i]) <= 90 or 97 <= ord(linha[i]) <= 122:
                caracter = maisculas_minusculas(linha[i])
                caracter_convertido = converte_letras_numeros(caracter)
                codigo_ofuscado += caracter_convertido
            else:
                codigo_ofuscado += linha[i]
        elif linha[i] == " ":
            for k in range(i, -1, -1):
                if linha[k] != " ":
                    codigo_ofuscado += "*"
        else:
            numero_convertido = converte_numeros_letras(linha[i])
            codigo_ofuscado += numero_convertido
    print(codigo_ofuscado)
    return codigo_ofuscado

def maisculas_minusculas(letra):
    if 65 <= ord(letra) <= 90:
        return chr((ord(letra)) + 32)
    return chr((ord(letra)) - 32)

def converte_letras_numeros(letra):
    if letra == "A" or letra == "a":
        return "4"
    elif letra == "B" or letra == "b":
        return "8"
    elif letra == "E" or letra == "e":
        return "3"
    elif letra == "G" or letra == "g":
        return "6"
    elif letra == "i" or letra == "i":
        return "1"
    elif letra == "L" or letra == "l":
        return "7"
    elif letra == "S" or letra == "s":
        return "5"
    elif letra == "O" or letra == "o":
        return "0"
    else:
        return letra

def converte_numeros_letras(numero):
    if numero == "4":
        return "A"
    elif numero == "8":
        return "B"
    elif numero == "3":
        return "E"
    elif numero == "6":
        return "G"
    elif numero == "1":
        return "I"
    elif numero == "7":
        return "L"
    elif numero == "5":
        return "S"
    elif numero == "0":
        return "O"
    else:
        return numero

def test_1():
    assert ofuscador("Tarso Jabbes") == "t4R50*****j48835"

def test_2():
    assert ofuscador("Prog 1") == "pR06****I"

def test_3():
    assert ofuscador("num3ros") == "NUMER05"

def test_4():
    assert ofuscador("M3u Test3") == "mEU***t35TE"

ofuscador("Tarso Jabbes")
ofuscador("Prog 1")
ofuscador("num3ros")
ofuscador("M3u Test3")
