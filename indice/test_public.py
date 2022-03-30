from undertst import indice_remissivo

def test_0_caso_base():
    texto = "eu prefiro que todos tirem notas boas do que eu ter que fazer um novo miniteste"
    indice = {"eu": [0, 9], "prefiro": [1], "que": [2, 8, 11], "todos": [3], "tirem": [4], "notas": [5], "boas": [6], "do": [7], "ter": [10], "fazer": [12], "um": [13], "novo": [14], "miniteste": [15]}
    assert set(indice_remissivo(texto)) == set(indice)
