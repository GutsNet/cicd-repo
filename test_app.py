import unittest
from app import sumar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

        self.assertEqual(restar(8, 5), 3)
        self.assertEqual(restar(3, 1), 2)

        self.assertEqual(multiplicar(2, 2), 4)
        self.assertEqual(multiplicar(7, 7), 49)

if __name__ == '__main__':
    unittest.main()
