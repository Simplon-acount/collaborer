# Fonction addition 
def add(a, b):
    return a + b


# Fonction soustraction 
def subtract(a, b):
    return a - b


# 3. Multiplication (utilise add)
def multiply(a, b):
    result = 0
    for _ in range(abs(b)):  
        result = add(result, a)
    if b < 0:
        result = -result
    return result

# 4. Division (avec gestion division par zéro)
def divide(a, b):
    if b == 0:
        return "Erreur : division par zéro impossible."
    return a / b