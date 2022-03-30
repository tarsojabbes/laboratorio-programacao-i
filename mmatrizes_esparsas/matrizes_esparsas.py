def soma_matrizes_esparsas(m1, m2):
    nova_matriz = [m1[0], m1[1]]
    dicionario = m1[2]
    for chave_valor in dicionario:
        dicionario[m2[2][m2[2]]] = "valor"
    print(dicionario)

M1 = (120, 200, {(115, 64): -5})
M2 = (120, 200, {(20, 55): 5})

soma_matrizes_esparsas(M1, M2)