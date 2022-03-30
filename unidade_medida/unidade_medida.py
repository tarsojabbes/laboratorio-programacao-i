# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

unidades = {"km": 1000, "hm": 100,
            "dam": 10, "m": 1,
            "dm": 0.1, "cm": 0.01,
            "mm": 0.001}

while True:
    valores = input().split()
    
    primeiro_valor = int(valores[0])
    unidade_primeiro = valores[1]
    segundo_valor = int(valores[2])
    unidade_segundo = valores[3]

    if primeiro_valor == 0 and segundo_valor == 0:
        break

    primeiro_metros = primeiro_valor * unidades[unidade_primeiro]
    segundo_metros = segundo_valor * unidades[unidade_segundo]
    valor_total = primeiro_metros + segundo_metros

    print(f"{valor_total:.2f} m")