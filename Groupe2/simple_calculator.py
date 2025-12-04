
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
   return a*b

def divide(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def power(a, b):
    result = 1
    for _ in range(b):
        result = multiply(result, a)
    return result

# Boucle interactive
