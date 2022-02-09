numero_adultos = int(input())
numero_criancas = int(input())
valor_ingresso = float(input())

total = (numero_adultos * valor_ingresso) + (numero_criancas * (valor_ingresso/2))

print(f"Total: R$ {total:.2f}")
