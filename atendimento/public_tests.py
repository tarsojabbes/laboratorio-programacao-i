import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global filas_de_atendimento
        undertest = __import__(module)
        filas_de_atendimento = getattr(undertest, 'filas_de_atendimento', None)

    def test_exemplo1(self):
        pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
        assert filas_de_atendimento(pacientes, 3) == [
            ['Andre', 'Carlos'],
            ['Antonio', 'Claudia'],
            ['Bianca']
        ]

    def test_exemplo2(self):
        pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos']
        assert filas_de_atendimento(pacientes, 2) == [
            ['Andre', 'Bianca'],
            ['Antonio', 'Carlos']
        ]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
