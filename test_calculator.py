import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Настройка тестов. Создание экземпляра калькулятора перед каждым тестом."""
        self.calc = Calculator()

    def test_add(self):
        """Тест сложения."""
        result = self.calc.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        """Тест вычитания."""
        result = self.calc.subtract(7, 4)
        self.assertEqual(result, 3)

    def test_multiply(self):
        """Тест умножения."""
        result = self.calc.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_divide(self):
        """Тест деления."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        """Тест деления на ноль."""
        with self.assertRaises(ValueError, msg="Нельзя делить на 0!!!"):
            self.calc.divide(5, 0)

    def test_square(self):
        """Тест возведения в квадрат."""
        result = self.calc.square(4)
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.main()
