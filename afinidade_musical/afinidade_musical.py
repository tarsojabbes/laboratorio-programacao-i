# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def tem_afinidade(l1,l2):
    comum_ambos = 0

    for artista in l1:
        for artista2 in l2:
            if artista == artista2:
                comum_ambos += 1
    
    if comum_ambos >= 3:
        return True
    return False

def test_1():
    l1 = ["a",'b','c','d']
    l2 = ['c', 'd', 'b']
    assert tem_afinidade(l1,l2) == True