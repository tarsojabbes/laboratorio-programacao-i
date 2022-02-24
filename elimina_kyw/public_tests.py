import unittest
import sys

module = sys.argv[-1].split(".py")[0]

def elimina_kyw(frase):
    nova_frase = ''

    for elemento in frase:
        if elemento == 'k' or elemento == 'y' or elemento == 'w':
            continue
        else:
            nova_frase += elemento
    
    return nova_frase

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global elimina_kyw
        undertest = __import__(module)
        elimina_kyw = getattr(undertest, 'elimina_kyw', None)

    def test_1_publico(self):
        s1 = 'kasayeww'
        s2 = 'makria bonita'

        assert elimina_kyw(s1) == 'asae'
        assert elimina_kyw(s2) == 'maria bonita'


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
