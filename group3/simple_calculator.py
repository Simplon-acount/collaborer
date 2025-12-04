# Fonction addition 
def add(a, b):
    return a + b


# Fonction soustraction 
def subtract(a, b):
    return a - b


# 3. Multiplication 
def multiply(a, b):
   return a*b

# 4. Division (avec gestion division par zéro)
def divide(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b