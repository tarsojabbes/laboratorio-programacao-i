# Computação - UFCG
# Programação 1
# Tarso Jabbes Lima de Oliveira

numero_a = int(input())
numero_b = int(input())
numero_c = int(input())

if numero_a <=  numero_b and numero_b <= numero_c:
    print(numero_a,numero_b, numero_c)
elif numero_a <= numero_c and numero_c <= numero_b:
    print(numero_a, numero_c,numero_b)
elif numero_b <= numero_a and numero_a <= numero_c:
    print(numero_b, numero_a, numero_c)
elif numero_b <= numero_c and numero_c <= numero_a:
    print(numero_b, numero_c, numero_a)
elif numero_c <= numero_b and numero_b <= numero_a:
    print(numero_c, numero_b, numero_a)
elif numero_c <= numero_a and numero_a <= numero_b:
    print(numero_c, numero_a, numero_b)
