palavra = input()

trocas = 0
palavra_criptografada = palavra[0]

for i in range(1, len(palavra)):
    if palavra[i] == 'a' or palavra[i] == "A":
        palavra_criptografada += "4"
        trocas += 1
    elif palavra[i] == 'e' or palavra[i] == 'E':
        palavra_criptografada += "3"
        trocas += 1
    elif palavra[i] == 'i' or palavra[i] == "I":
        palavra_criptografada += "1"
        trocas += 1
    elif palavra[i] == 'o' or palavra[i] == 'O':
        palavra_criptografada += "0"
        trocas += 1
    else:
        palavra_criptografada += palavra[i]

print(f"{palavra_criptografada} ({trocas} troca(s))")

