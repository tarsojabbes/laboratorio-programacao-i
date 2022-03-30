# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220
# Prova 2 | Data: 21 de Março de 2022

# Resumo: programa que checa 3 condições de parada: quando se lê 6 números ímpares,
# quando a soma dos lidos for maior ou igual ao valor limite
# ou quando se chega ao final da sequência.

# Entrada: sequência de números inteiros e um valor limite de soma.
# Saída: soma dos números lídos, quantidade dos números lidos e o critério de parada.

sequencia = input()
valor_limite = int(input())

quantidade_numeros_impares = 0
soma = 0
parada = ''

iterador = 0
while iterador < len(sequencia):
    numero_analisado = int(sequencia[iterador])
    soma += numero_analisado

    if not numero_analisado%2==0:
        quantidade_numeros_impares += 1
        if quantidade_numeros_impares >= 6:
            parada = "6 ímpares"
            break

    if soma >= valor_limite:
        parada = "limite"
        break

    parada = "final da sequência"
    iterador += 1

print(f"soma: {soma}")

if parada == "final da sequência":
    print(f"números lidos: {len(sequencia)} de {len(sequencia)}")
else:
    print(f"números lidos: {iterador+1} de {len(sequencia)}")
    
print(f"critério de parada: {parada}")
