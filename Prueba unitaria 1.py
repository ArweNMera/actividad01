import unittest

class X:
    def sumar(self, x, y):
        return x + y


class TestOperacionesBasicas(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.x = X()

    def test_sumar(self):
        """Prueba unitaria para la operación de suma."""
        resultado = self.x.sumar(5, 3)
        self.assertEqual(resultado, 8, "La suma de 5 + 3 debería ser 8")


if __name__ == "__main__":
    unittest.main()
