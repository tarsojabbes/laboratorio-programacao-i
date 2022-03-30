# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220
# Prova de Reposição | Data: 30 de Março de 2022

# Resumo: um programa que recebe uma lista de valores
# e retorna uma segunda lista que contém as somas de valores
# simetricamente opostos da lista recebida

# Parâmetro da função: uma lista de valores inteiros
# Retorno da função: uma lista com as somas dos valores simetricamente opostos

def soma_simetricos(valores):
    soma = []
    for i in range(len(valores)//2):
        valor_direita, valor_esquerda = seleciona_opostos(valores, i)
        soma_valores = valor_direita + valor_esquerda
        soma.append(soma_valores)
    
    if len(valores)%2 != 0:
        soma.append(valores[len(valores)//2])

    return soma

def seleciona_opostos(valores, indice):
    valor_direita = valores[len(valores)-indice-1]
    valor_esquerda = valores[indice]
    return valor_direita, valor_esquerda

def test_1():
    assert soma_simetricos([2, 7, 3, 9, 6, 4]) == [6, 13, 12]

def test_2():
    assert soma_simetricos([11, 12, 13, 7, 8, 9]) == [20, 20, 20]

def test_3():
    assert soma_simetricos([0]) == [0]

def test_4():
    assert soma_simetricos([1, 2, 3, 2, 1]) == [2, 4, 3]
    
def test_5():
    assert soma_simetricos([]) == []

def test_6():
    assert soma_simetricos([7, 9, 11, 13, 15]) == [22, 22, 11]

def test_7():
    assert soma_simetricos([7, 9, 11, 13, 15, 17]) == [24, 24, 24]

def test_8():
    assert soma_simetricos([-7, -9, 11, 13, 15, 17]) == [10, 6, 24]

def test_9():
    assert soma_simetricos([0, 0, 0]) == [0, 0]

def test_10():
    assert soma_simetricos([0, 0]) == [0]

def test_11():
    assert soma_simetricos([-1, 1, -2, 2, -3, 3, -3]) == [-4, 4, -5, 2]

