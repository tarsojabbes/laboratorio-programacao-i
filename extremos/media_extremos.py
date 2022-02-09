# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

quantidade_numeros = int(input())

numeros = []
maior = 0
menor = 0

for i in range(quantidade_numeros):
    numero = int(input())
    numeros.append(numero)

    if i == 0:
        menor = numero
        maior = numero

    if numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero

media = (maior + menor)/2

acima_media = 0
abaixo_media = 0 
for numero in numeros:
    if numero > media:
        acima_media+=1
    elif numero < media:
        abaixo_media += 1

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Média dos extremos: {media:.2f}")
print(f"{abaixo_media} número(s) abaixo da média")
print(f"{acima_media} número(s) acima da média")


