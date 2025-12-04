def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division par zéro interdite")
    return a / b