def bubblesort(dados):
    for j in range(len(dados)):
        swapped = False
        for i in range(len(dados) - 1):
            if dados[i] > dados[i+1]:
                dados[i], dados[i+1] = dados[i+1], dados[i]
                swapped =  True
        if not swapped:
            return