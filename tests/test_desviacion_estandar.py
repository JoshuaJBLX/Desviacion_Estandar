class TestDesviacionEstandar(unittest.TestCase):
    def test_desviacion_estandar_un_elemento(self):
        numeros = [5]
        desviacion_esperada = 0.0
        desviacion_actual = calcular_desviacion_estandar(numeros)
        self.assertAlmostEqual(desviacion_esperada, desviacion_actual, places=2)
