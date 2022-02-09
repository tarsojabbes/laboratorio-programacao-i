# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

palavras_lidas = 0

while True:
    palavra = input().lower()
    palavras_lidas += 1

    quantidade_vogais = 0
    quantidade_consoantes = 0

    iterador = 0
    while iterador < len(palavra):
        letra = palavra[iterador]
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            quantidade_vogais += 1
        else:
            quantidade_consoantes += 1
        iterador += 1
    
    if quantidade_consoantes > quantidade_vogais: break

print(palavras_lidas)
    
