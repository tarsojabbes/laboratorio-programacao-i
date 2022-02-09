# Computação - UFCG
# Programação 1
# Tarso Jabbes Lima de Oliveira

area = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

iptu = (area * aliquota) + 35

iptu_quota_unica = 0.75 * iptu

total_seis_parcelas = 0.95 * iptu
valor_parcela_seis= total_seis_parcelas/6

valor_parcela_dez = iptu/10

print(f"IPTU: R$ {iptu:.2f}\n")
print(f"Pagamento:")
print(f"1. Quota única. R$ {iptu_quota_unica:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {total_seis_parcelas:.2f}")
print(f"   6 x R$ {valor_parcela_seis:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {iptu:.2f}")
print(f"   10 x R$ {valor_parcela_dez:.2f}")
