def busca(seq, num):

    for i in (range(len(seq))):
        if seq[i] == num:
            return i
    return -1
