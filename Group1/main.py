def add(a, b):
    return a + b

def multiply(a, b):
    """Multiplie a et b en utilisant uniquement la fonction add."""
    if a == 0 or b == 0:
        return 0
    
    # Gérer le signe
    negative = (a < 0) ^ (b < 0)  # XOR : vrai si un seul est négatif
    a, b = abs(a), abs(b)

    result = 0
    for _ in range(b):
        result = add(result, a)
    
    return -result if negative else result

def divide(a, b):
    """Divise a par b. Renvoie None (ou un message) si division par zéro."""
    if b == 0:
        print("Erreur : Division par zéro impossible.")
        return None  # ou raise ValueError("Division par zéro")
    return a / b




print(multiply(3, 4))    # 12
print(multiply(-2, 5))   # -10
print(multiply(0, 100))  # 0

print(divide(10, 2))     # 5.0
print(divide(5, 0))      # Erreur : Division par zéro impossible. + None