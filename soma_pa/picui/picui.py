# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

recorde = float(input())
quantidade = float(input())

if quantidade > recorde:
    print(f"recorde quebrado ({quantidade:.2f} kg)")
elif quantidade < recorde:
    print("recorde mantido")
else:
    print("recorde empatado")
