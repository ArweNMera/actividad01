import unittest


class X:

    def restar(self, x, y):
        return x - y


class TestOperacionesBasicas(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.x = X()


    def test_restar(self):
        """Prueba unitaria para la operación de resta."""
        resultado = self.x.restar(10, 4)
        self.assertEqual(resultado, 6, "La resta de 10 - 4 debería ser 6")


if __name__ == "__main__":
    unittest.main()
