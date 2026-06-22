#TESTEO DE FUNCIONES
# test_funciones.py
import unittest
from primos import es_primo_division_ensayo, explicar_no_primo_DS, es_primo_fermat, explicar_no_primo_TF,es_primo_miller_rabin,explicar_no_primo_MR

# TESTEO DE PRIMALIDAD POR DIVISIÓN ENSAYO
class TestPrimalidad(unittest.TestCase):

    def test_numeros_primos(self):
        self.assertTrue(es_primo_division_ensayo(5))
        self.assertTrue(es_primo_division_ensayo(13))

    def test_numeros_compuestos(self):
        self.assertFalse(es_primo_division_ensayo(4))
        self.assertFalse(es_primo_division_ensayo(9))

    def test_casos_por_borde(self):
        self.assertFalse(es_primo_division_ensayo(0))
        self.assertFalse(es_primo_division_ensayo(1))
        self.assertFalse(es_primo_division_ensayo(-7))

# TESTEO DE NO PRIMALIDAD POR DIVISIÓN ENSAYO
class TestNoPrimalidad(unittest.TestCase):

    def test_numeros_primos(self):
        # assertTrue verifica que el resultado sea True
        self.assertTrue(explicar_no_primo_DS(6))
        self.assertTrue(explicar_no_primo_DS(14))

    def test_numeros_compuestos(self):
        self.assertIsInstance(explicar_no_primo_DS(4),str)
        self.assertIsInstance(explicar_no_primo_DS(9),str)

    def test_casos_por_borde(self):
        self.assertIsInstance(explicar_no_primo_DS(0),str)
        self.assertIsInstance(explicar_no_primo_DS(1),str)
        self.assertIsInstance(explicar_no_primo_DS(-7),str)
#************************************************************************************************
# TESTEO DE PRIMALIDAD POR TEST DE FERMAT
class TestPrimalidad(unittest.TestCase):
    def test_numeros_primos(self):
        self.assertTrue(es_primo_fermat(5))
        self.assertTrue(es_primo_fermat(13))

    def test_numeros_compuestos(self):
        self.assertFalse(es_primo_fermat(4))
        self.assertFalse(es_primo_fermat(9))

    def test_casos_por_borde(self):
        self.assertFalse(es_primo_fermat(0))
        self.assertFalse(es_primo_fermat(1))
        self.assertFalse(es_primo_fermat(-7))

# TESTEO DE NO PRIMALIDAD POR TEST DE FERMAT
class TestNoPrimalidad(unittest.TestCase):

    def test_numeros_primos(self):
        
        self.assertTrue(explicar_no_primo_TF(6))
        self.assertTrue(explicar_no_primo_TF(14))

    def test_numeros_compuestos(self):
        
        self.assertIsInstance(explicar_no_primo_TF(4),str)
        self.assertIsInstance(explicar_no_primo_TF(9),str)

    def test_casos_por_borde(self):
        self.assertIsInstance(explicar_no_primo_TF(0),str)
        self.assertIsInstance(explicar_no_primo_TF(1),str)
        self.assertIsInstance(explicar_no_primo_TF(-7),str)

#************************************************************************************************
# TESTEO DE PRIMALIDAD POR TEST DE MILLER-RABIN
class TestPrimalidad(unittest.TestCase):
    def test_numeros_primos(self):
        self.assertTrue(es_primo_miller_rabin(5))
        self.assertTrue(es_primo_miller_rabin(13))

    def test_numeros_compuestos(self):
        self.assertFalse(es_primo_miller_rabin(4))
        self.assertFalse(es_primo_miller_rabin(9))

    def test_casos_por_borde(self):
        self.assertFalse(es_primo_miller_rabin(0))
        self.assertFalse(es_primo_miller_rabin(1))
        self.assertFalse(es_primo_miller_rabin(-7))

# TESTEO DE NO PRIMALIDAD POR TEST DE MILLER-RABIN
class TestNoPrimalidad(unittest.TestCase):

    def test_numeros_primos(self):
        
        self.assertTrue(explicar_no_primo_MR(6))
        self.assertTrue(explicar_no_primo_MR(14))

    def test_numeros_compuestos(self):
        
        self.assertIsInstance(explicar_no_primo_MR(4),str)
        self.assertIsInstance(explicar_no_primo_MR(9),str)

    def test_casos_por_borde(self):
        self.assertIsInstance(explicar_no_primo_MR(0),str)
        self.assertIsInstance(explicar_no_primo_MR(1),str)
        self.assertIsInstance(explicar_no_primo_MR(-7),str)


if __name__ == '__main__':
    unittest.main()
