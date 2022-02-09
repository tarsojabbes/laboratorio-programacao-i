# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

vendedor = input("Qual é o nome do(a) vendedor(a)? ")
valor_da_venda = float(input("Qual é o valor da venda? "))

if valor_da_venda > 500:
    comissao = valor_da_venda * 0.1
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor:.5s} é R$ {comissao:.2f}.")
else:
    comissao = valor_da_venda * 0.05
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor} é R$ {comissao:.2f}.")

