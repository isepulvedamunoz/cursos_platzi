import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaCristaltest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 18

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)
    
    def test_es_menor_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()