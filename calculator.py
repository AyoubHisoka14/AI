

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

if __name__ == '__main__':
    calculator = Calculator()
    result_add = calculator.add(5, 3)
    result_subtract = calculator.subtract(10, 4)
    result_multiply = calculator.multiply(6, 7)
    result_divide = calculator.divide(8, 2)

    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")
    print(f"Multiplication: {result_multiply}")
    print(f"Division: {result_divide}")