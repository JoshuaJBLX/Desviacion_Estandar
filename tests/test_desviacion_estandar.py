class TestDesviacionEstandar(unittest.TestCase):
    def test_desviacion_estandar_conjunto_vacio(self):
        numeros = []
        with self.assertRaises(ValueError):
            calcular_desviacion_estandar(numeros)
