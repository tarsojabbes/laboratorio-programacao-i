# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

minutos_chamada = int(input())

valor = 1

if minutos_chamada <= 3:
    valor += 0.5 * minutos_chamada
else:
    blocos_cinco_minutos = minutos_chamada//5
    minutos_restantes = minutos_chamada%5
    valor += (minutos_restantes * 0.7) + (blocos_cinco_minutos*3)

print(f"R$ {valor:.2f}")
