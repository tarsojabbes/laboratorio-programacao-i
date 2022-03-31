# Computação - UFCG
# Programação 1 - 2021.1e
# Tarso Jabbes Lima de Oliveira | Matrícula: 121110220

def filas_de_atendimento(fila_unica, n):
    fila_final = []
    for i in range(n):
        fila_medico = []
        fila_final.append(fila_medico)
    print(fila_final)

    indice = 0
    indice_paciente = len(fila_unica)
    for j in range(len(n)):
        indice += 1
    print(fila_final)

pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
filas_de_atendimento(pacientes, 3)