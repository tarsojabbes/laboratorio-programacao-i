# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def eh_roteiro(iata, voos, rota):
    rota = rota.split("/")
    
    partida = iata[rota[0]]
    escala = iata[rota[1]]
    destino = iata[rota[2]]

    for valor in voos[partida]:
        if valor == escala:
            for valor2 in voos[escala]:
                if valor2 == destino:
                    return True
    
    return False
