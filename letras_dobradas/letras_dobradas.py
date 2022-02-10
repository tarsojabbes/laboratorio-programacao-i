# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

quantidade_palavras = int(input())

palavras = []
for i in range(quantidade_palavras):
    palavra = input()
    palavras.append(palavra)

letras_repetidas = []
nao_repetida = []

for palavra in palavras:
    antes = None
    tem_repetida =  False
    for char in palavra:
        if antes == char:
            letras_repetidas.append(palavra)
            tem_repetida = True
            break

        antes = char
    if not tem_repetida:
        nao_repetida.append(palavra)
        

print(f"{len(letras_repetidas)} palavra(s) com letras dobradas:")
for palavra in letras_repetidas:
    print(palavra)
print("---")
print(f"{len(nao_repetida)} palavra(s) sem letras dobradas:")
for palavra in nao_repetida:
    print(palavra)