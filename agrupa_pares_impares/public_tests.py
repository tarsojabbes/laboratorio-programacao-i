import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global agrupa_pares_impares
        undertest = __import__(module)
        agrupa_pares_impares = getattr(undertest, 'agrupa_pares_impares', None)

    def test_publico(self):
        seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]
        agrupa_pares_impares(seq)
        assert seq == [6, 12, 6, 8, 14, 10, 15, 3, 25, 1, 7]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
