import math

def add(a,b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
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


def simple_calculator_interface():
    while True:
        print("\nOpérations disponibles: add, subtract, multiply, divide, power, quit")
        op = input("Choisissez une opération: ").strip().lower()
        if op == "quit":
            break
        a = int(input("Entrez le premier nombre: "))
        b = int(input("Entrez le deuxième nombre: "))

        if op == "add":
            print("Résultat:", add(a, b))
        elif op == "subtract":
            print("Résultat:", subtract(a, b))
        elif op == "multiply":
            print("Résultat:", multiply(a, b))
        elif op == "divide":
            print("Résultat:", divide(a, b))
        elif op == "power":
            print("Résultat:", power(a, b))
        else:
            print("Opération invalide")

