# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

angulo = float(input())

if angulo > 360:
    angulo = angulo % 360

quadrante = 0

if 0 < angulo < 90:
    quadrante = 1
elif 90 < angulo < 180:
    quadrante = 2
elif 180 < angulo < 270:
    quadrante = 3
elif 270 < angulo < 360:
    quadrante = 4

if quadrante == 0:
    print("Sobre eixos")
else:
    print(f"Quadrante {quadrante}")
