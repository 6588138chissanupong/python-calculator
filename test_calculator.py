import unittest
from calculator import Calculator  

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 9), -5)
        self.assertEqual(self.calc.subtract(9, 4), 5)
        self.assertEqual(self.calc.subtract(9, -4), 13)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 7), 49)
        self.assertEqual(self.calc.multiply(-7, 7), -49)
        self.assertEqual(self.calc.multiply(-7, -7), 49)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
