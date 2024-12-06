import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_add_and_subtract(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(calc.subtract(result, 1), 4)

if __name__ == '__main__':
    unittest.main()