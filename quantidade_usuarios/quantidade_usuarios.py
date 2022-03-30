# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def quantidade_usuarios(cadastro):
    quantidade_usuarios = 0
    for valor in cadastro:
        for usuario in cadastro[valor]:
            if usuario != "administrador":
                quantidade_usuarios += 1
    return quantidade_usuarios
