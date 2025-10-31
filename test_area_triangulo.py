import unittest
import math
from src.area_triangulo import area_triangulo

class TestAreaTriangulo(unittest.TestCase):
    # Casos válidos
    def test_area_normal(self):
        self.assertAlmostEqual(area_triangulo(10, 5), 25.0)

    def test_area_flotantes(self):
        self.assertAlmostEqual(area_triangulo(3.5, 2.1), 3.675)

    def test_area_minimo_valido(self):
        self.assertAlmostEqual(area_triangulo(0.0001, 0.0001), 0.000000005)

    def test_area_numeros_grandes(self):
        self.assertAlmostEqual(area_triangulo(1e6, 2e6), 1e12)

    # Casos inválidos: valores límite
    def test_base_cero(self):
        with self.assertRaises(ValueError):
            area_triangulo(0, 5)

    def test_altura_cero(self):
        with self.assertRaises(ValueError):
            area_triangulo(5, 0)

    def test_valores_negativos(self):
        with self.assertRaises(ValueError):
            area_triangulo(-3, 5)

    # Casos inválidos: tipos incorrectos
    def test_tipos_invalidos(self):
        with self.assertRaises(TypeError):
            area_triangulo("3", 5)
        with self.assertRaises(TypeError):
            area_triangulo(3, None)
        with self.assertRaises(TypeError):
            area_triangulo([], 5)

    # Casos inválidos: infinitos o NaN
    def test_valores_infinitos(self):
        with self.assertRaises(ValueError):
            area_triangulo(math.inf, 5)

    def test_valores_nan(self):
        with self.assertRaises(ValueError):
            area_triangulo(math.nan, 5)


if __name__ == "__main__":
    unittest.main()


        
      