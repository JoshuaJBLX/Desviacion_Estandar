import unittest
from src.desviacion_estandar import calcular_desviacion_estandar

class TestDesviacionEstandar(unittest.TestCase):
    def test_desviacion_estandar_basico(self):
        numeros = [2, 4, 6, 8, 10]
        desviacion_esperada = 2.8284271247461903
        desviacion_actual = calcular_desviacion_estandar(numeros)
        self.assertAlmostEqual(desviacion_esperada, desviacion_actual, places=2)
