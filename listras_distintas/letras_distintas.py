# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220
# Conta letras distintas entre duas palavras

primeira_palavra = input()
segunda_palavra = input()

quantidade_letras_distintas = 0

for letra in primeira_palavra:

    letra_presente = False

    for char in segunda_palavra:
        if letra == char:
            letra_presente = True
            break

    if not letra_presente:
        quantidade_letras_distintas += 1


print(quantidade_letras_distintas)