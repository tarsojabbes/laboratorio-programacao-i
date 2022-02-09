# Computação - UFCG
# Programação 1
# Aluno: Tarso Jabbes Lima de Oliveira

cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

# primeiro cpf
primeira_parte_cpf1 = cpf1//100
segunda_parte_cpf1 = cpf1%100

penultimo_digito_cpf1 = segunda_parte_cpf1//10
ultimo_digito_cpf1 = segunda_parte_cpf1%10

soma_cpf1 = penultimo_digito_cpf1 + ultimo_digito_cpf1

# segundo cpf
primeira_parte_cpf2 = cpf2//100
segunda_parte_cpf2 = cpf2%100

penultimo_digito_cpf2 = segunda_parte_cpf2//10
ultimo_digito_cpf2 = segunda_parte_cpf2%10

soma_cpf2 = penultimo_digito_cpf2 + ultimo_digito_cpf2

#terceiro cpf
primeira_parte_cpf3 = cpf3//100
segunda_parte_cpf3 = cpf3%100

penultimo_digito_cpf3 = segunda_parte_cpf3//10
ultimo_digito_cpf3 = segunda_parte_cpf3%10

soma_cpf3= penultimo_digito_cpf3 + ultimo_digito_cpf3

print(f"{primeira_parte_cpf1}-{segunda_parte_cpf1}")
print(soma_cpf1)


print(f"{primeira_parte_cpf2}-{segunda_parte_cpf2}")
print(soma_cpf2)

print(f"{primeira_parte_cpf3}-{segunda_parte_cpf3}")
print(soma_cpf3)
