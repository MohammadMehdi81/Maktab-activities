def inp(number1, operation, number2):
    if operation == '+':
        return add(number1, number2)
    if operation == '-':
        return subtract(number1, number2)
    if operation == '/':
        return divide(number1, number2)
    if operation == '*':
        return multiply(number1, number2)


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
