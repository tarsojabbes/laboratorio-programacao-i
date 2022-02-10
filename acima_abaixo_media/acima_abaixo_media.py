# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

soma_valores = 0
valores = []
while True:
    valor = float(input())

    if soma_valores + valor > 100 or valor < 0: break

    soma_valores += valor
    valores.append(valor)

if len(valores) > 0:
    media = soma_valores/len(valores)

    for valor in valores:
        if valor > media:
            print(f"{int(valor)} > {media:.3f}")
        elif valor < media:
            print(f"{int(valor)} < {media:.3f}")
