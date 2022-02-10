valores_inseridos = []

soma_valores = 0

while True:
    valor = input()

    if valor == "fim": break

    valor_inteiro = int(valor)
    valores_inseridos.append(valor_inteiro)
    soma_valores += valor_inteiro

quantidade_valores = len(valores_inseridos)
media = soma_valores/quantidade_valores

print(f"{media:.2f}")

for i in range(0, len(valores_inseridos)):
    if valores_inseridos[i] < media:
        print(f"{i + 1} {valores_inseridos[i]}")
