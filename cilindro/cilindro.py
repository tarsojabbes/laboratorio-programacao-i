# Computação - UFCG
# Programação 1
# Aluno: Tarso Jabbes Lima de Oliveira

print("Cálculo da Superfície de um Cilindro")
print("---")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

area_base = 3.14159 * ((diametro/2) ** 2)
area_lateral = (2 * 3.14159 * (diametro/2)) * altura

area_total = area_lateral + (2 * area_base)

print("---")
print(f"Área calculada: {area_total:.2f}")
