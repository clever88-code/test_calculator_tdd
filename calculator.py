class Calculator:
    def add(self, x, y):
        """Сложение двух чисел."""
        return x + y

    def subtract(self, x, y):
        """Вычитание второго числа из первого."""
        return x - y

    def multiply(self, x, y):
        """Умножение двух чисел."""
        return x * y

    def divide(self, x, y):
        """Деление первого числа на второе. Выбрасывает ValueError, если деление на 0."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def square(self, x):
        """Возводит число в квадрат."""
        return x ** 2
