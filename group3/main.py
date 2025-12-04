# main.py
import pandas as pd

# 12. Importer toutes les fonctions
from simple_calculator import add, subtract, multiply, divide, power
from stat_calculator import normalise, mod, averageMed, moreDispersed, maxMin, dfStats

# -------------------------------------
#      Menu pour le simple calculator
# -------------------------------------
def menu_simple_calculator():
    print("\n--- Simple Calculator ---")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Power")
    print("0 - Back")

    choice = input("Enter your choice: ")

    if choice == "0":
        return

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
        print("Invalid choice!")


# -------------------------------------
#      Menu pour le statistical calculator
# -------------------------------------
def menu_stat_calculator():
    print("\n--- Statistical Calculator ---")

    print("Entrez deux listes de nombres séparées par des virgules pour créer deux DataFrames")

    data1 = list(map(float, input("DF1 Values: ").split(",")))
    data2 = list(map(float, input("DF2 Values: ").split(",")))

    df1 = pd.DataFrame({"values": data1})
    df2 = pd.DataFrame({"values": data2})

    print("\n1 - Normalise")
    print("2 - Mode")
    print("3 - Average & Median")
    print("4 - More Dispersed")
    print("5 - Max & Min")
    print("6 - dfStats (All combined)")
    print("0 - Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("DF1 normalized:\n", normalise(df1))
        print("DF2 normalized:\n", normalise(df2))

    elif choice == "2":
        m1, m2 = mod(df1, df2)
        print("Mode DF1:\n", m1)
        print("Mode DF2:\n", m2)

    elif choice == "3":
        avg1, med1 = averageMed(df1)
        avg2, med2 = averageMed(df2)
        print(f"DF1 - Average: {avg1.values[0]}, Median: {med1.values[0]}")
        print(f"DF2 - Average: {avg2.values[0]}, Median: {med2.values[0]}")

    elif choice == "4":
        print("More dispersed:", moreDispersed(df1, df2))

    elif choice == "5":
        numbers = data1 + data2
        mx, mn = maxMin(numbers)
        print(f"Max: {mx}, Min: {mn}")

    elif choice == "6":
        results = dfStats(df1, df2)
        print("\n--- dfStats Results ---")
        for key, value in results.items():
            print(f"\n{key}:\n{value}")

    else:
        print("Invalid choice!")


# -------------------------------------
#            MAIN MENU
# -------------------------------------
while True:
    print("\n========= SUPER CALCULATOR =========")
    print("1 - Simple Calculator")
    print("2 - Statistical Calculator")
    print("0 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        menu_simple_calculator()
    elif choice == "2":
        menu_stat_calculator()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")