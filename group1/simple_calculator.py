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
def power(a, b):
    """Retourne a élevé à la puissance b."""
    return a ** b

def interactive_loop():
    """Boucle interactive pour tester les fonctions du simple_calculator."""
    print("Bienvenue dans le Simple Calculator interactif !")
    print("Opérations disponibles : add, sub, mul, div, power, quit")

    while True:
        op = input("Choisissez une opération : ").strip().lower()
        if op == "quit":
            print("Au revoir !")
            break
        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")
            continue

        if op == "add":
            from simple_calculator import add
            print("Résultat :", add(a, b))
        elif op == "sub":
            from simple_calculator import sub
            print("Résultat :", sub(a, b))
        elif op == "mul":
            from simple_calculator import mul
            print("Résultat :", mul(a, b))
        elif op == "div":
            from simple_calculator import div
            try:
                print("Résultat :", div(a, b))
            except ZeroDivisionError as e:
                print("Erreur :", e)
        elif op == "power":
            print("Résultat :", power(a, b))
        else:
            print("Opération inconnue !")