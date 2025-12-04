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

        return "Erreur : division par zéro"
    return a / b

# 5. Puissance (a élevé à la puissance b)
def power(a, b):
    if b == 0:
        return 1

    if b < 0:
        if a == 0:
            return "Erreur : 0 ne peut être élevé à une puissance négative."
        result = 1
        for _ in range(-b):
            result = multiply(result, a)
        return divide(1, result)

    result = 1
    for _ in range(b):
        result = multiply(result, a)
    return result

# Interface utilisateur simple
while True:
    print("\nChoose an operation:")
    print("1 - add")
    print("2 - subtract")
    print("3 - multiply")
    print("4 - divide")
    print("5 - power")
    print("0 - exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Goodbye!")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    elif choice == "5":
        print("Result:", power(a, b))
    else:
        print("Invalid choice, try again!")
=======
        return "Erreur : division par zéro impossible."
    return a / b
