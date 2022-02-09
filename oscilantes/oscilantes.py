# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

codigo = input()

valido = False

for i in range(len(codigo) - 1):
    if codigo[i] == codigo[i + 1]:
        valido = False
    else:
        if int(codigo[i]) % 2 == 0 and int(codigo[i + 1]) % 2 != 0:
            valido = True
        elif int(codigo[i]) % 2  != 0 and int(codigo[i + 1]) % 2 == 0:
            valido = True

if valido == True:
    print(f"verdadeiro: {len(codigo)} algarismos.")
else:
    print(f"falso: {len(codigo)} algarismos.")
