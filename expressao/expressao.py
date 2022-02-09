# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

a = int(input())
b = int(input())
c = int(input())
d = int(input())

dc = int(str(d) + str(c))
ca = int(str(c) + str(a))
bb = int(str(b) + str(b))
aad = int(str(a) + str(a) + str(d))

resultado = dc - a - b - ca - d + bb + aad

print(resultado)
