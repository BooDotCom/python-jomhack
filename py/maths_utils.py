def add(a,b):
    """Add two numbers"""
    return a+b

def subtract(a,b):
    """Subtract two numbers"""
    return a-b

def multiply(a,b):
    """Multiply two numbers"""
    return a*b

def divide(a,b):
    """Divide two numbers"""
    return a/b

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n-1)

PI = 3.14159

class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, operation, a, b):
        if operation == "add":
            result = add(a,b)
        elif operation == "subtract":
            result = subtract(a,b)
        elif operation == "multiply":
            result = multiply(a,b)
        elif operation == "divide":
            result = divide(a,b)
        else:
            result = None

        self.history.append(f"{operation}({a}, {b}) = {result}")
        return result