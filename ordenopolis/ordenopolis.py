# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

resultado = []

while True:
    nome1 = input("nome 1? ")
    nome2 = input("nome 2? ")
    nome3 = input("nome 3? ")
      
    if not nome1 < nome2 < nome3:
        print("nomes inválidos: tente novamente") 
    else:
        resultado.append(nome1)
        resultado.append(nome2)
        resultado.append(nome3)
        break

print(f"{resultado[0]} {resultado[1]} de {resultado[2]}")




