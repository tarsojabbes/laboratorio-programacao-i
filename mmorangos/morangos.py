# Computação - UFCG
# Programação 1
# Tarso Jabbes Lima de Oliveira


quantidade = int(input())

caixas = quantidade//400
resto = ((quantidade%400)/quantidade) * 100

print(f"{caixas} caixa(s) completa(s) para embalar os morangos.")
print(f"{resto:.1f}% dos morangos serão perdidos.")
