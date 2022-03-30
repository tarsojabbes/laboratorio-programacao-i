def idosos_inicio(lista):

    indice_insercao = 0
    for i in range(len(lista)):
        if lista[i]>= 60:
            lista[i], lista[indice_insercao] = lista[indice_insercao], lista[i]
            indice_insercao += 1
