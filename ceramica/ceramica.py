# Computação - UFCG
# Programação 1
# Tarso Jabbes Lima de Oliveira

import math

capacidade_revestimento = float(input("Capacidade de revestimento? "))

print("\n== Dados do vão a revestir ==")

comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

area_lateral = (comprimento * altura) + (comprimento*altura) + (largura * altura) + (largura * altura) + (largura * comprimento)
numero_de_caixas = math.ceil(area_lateral/capacidade_revestimento)

print("\n== Resultados ==")
print(f"Área total a revestir: {area_lateral:.1f} m2")
print(f"Número de caixas: {numero_de_caixas}")

