import unittest


# Definimos una clase que representa el comportamiento que queremos probar.
class X:
    """
    Clase X con un método para multiplicar dos números.
    Si el segundo número es 0, simplemente devuelve el primer número
    para evitar una división o multiplicación inválida.
    """

    def z(self, a, b):
        """
        Realiza la multiplicación de 'a' y 'b', pero si 'b' es 0,
        devuelve solo 'a' como una forma de evitar la multiplicación con 0.

        Parámetros:
        a -- Primer número
        b -- Segundo número, si es 0 se devuelve solo 'a'

        Retorno:
        El resultado de la multiplicación o 'a' si 'b' es 0.
        """
        if b == 0:
            return a  # Se evita la operación con 0
        return a * b  # Multiplicación normal si b no es 0


# Definimos una clase de prueba para verificar el comportamiento de la clase X.
class TestX(unittest.TestCase):
    """
    Esta clase contiene pruebas unitarias para validar el comportamiento del método z de la clase X.
    """

    def test_multiplication(self):
        """
        Prueba que el método z realice una multiplicación correcta cuando
        ambos números son mayores que 0.
        """
        obj = X()
        self.assertEqual(obj.z(2, 3), 6)  # 2 * 3 = 6

    def test_no_zero_division(self):
        """
        Prueba que el método z maneje correctamente el caso en que el segundo
        número es 0, devolviendo solo el primer número.
        """
        obj = X()
        self.assertEqual(obj.z(2, 0), 2)  # Si el segundo es 0, devuelve el primero


# Ejecuta las pruebas cuando el archivo se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
