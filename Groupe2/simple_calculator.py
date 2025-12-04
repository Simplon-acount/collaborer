import math

def add(a,b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    """Multiply using repeated addition"""
    result = 0
    negative = False
    if b < 0:
        b = -b
        negative = True

    for _ in range(int(b)):
        result = add(result, a)


    if negative:
        result = -result




def divide(a,b):
    if (b != 0):
        return a / b
    else:
        return "Erreur : division par zéro impossible."

def power(a, b):
    result = 1
    if b >= 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result *= a
        result = 1 / result
    return result

# Boucle interactive
while True:
    print("\n=== Simple Calculator ===")
    print("Choisissez une opération :")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Puissance (^)")
    print("q. Quitter")

    choice = input("Votre choix : ")

    if choice.lower() == 'q':
        print("Au revoir !")
        break

    if choice not in ['1', '2', '3', '4', '5']:
        print("Choix invalide, réessayez.")
        continue

    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        continue

    if choice == '1':
        print(f"Résultat : {add(a, b)}")
    elif choice == '2':
        print(f"Résultat : {subtract(a, b)}")
    elif choice == '3':
        print(f"Résultat : {multiply(a, b)}")
    elif choice == '4':
        result = divide(a, b)
        print(f"Résultat : {result}")
    elif choice == '5':
        # Pour power, on convertit b en int (exposant entier)
        try:
            b_int = int(b)
            print(f"Résultat : {power(a, b_int)}")
        except ValueError:
            print("L'exposant doit être un entier.")

