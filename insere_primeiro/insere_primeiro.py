def insere_ordenado_primeiro(lista):
    for i in range(len(lista) -1, -1, -1):
        if lista[0] > lista[i]:
            lista[0], lista[i] = lista[i], lista[0]
