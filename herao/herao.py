# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

import math

n = int(input())

areas = 0
maiores_que_cem = 0
area_maiores_cem = 0

for i in range(n):
    lados = input().split()

    a = float(lados[0])
    b = float(lados[1])
    c = float(lados[2])

    semiperimetro = (a + b + c)/2

    area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

    if area > 100:
        maiores_que_cem += 1
        area_maiores_cem += area

    areas += area

    print(f"Área {i + 1}: {area:.2f}")


if maiores_que_cem > 0:
    media_maiores_cem = area_maiores_cem/maiores_que_cem
    print(f"Número maiores: {maiores_que_cem}, área média: {media_maiores_cem:.2f}")

