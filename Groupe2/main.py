import pandas as pd
from simple_calculator import add, subtract, multiply, divide, power, simple_calculator_interface
from stat_calculator import mean, median, mode, maximum, minimum

def main():
    print("=== Super Calculateur ===")
    while True:
        print("\nOptions :")
        print("1 - Calcul simple interactif")
        print("2 - Statistiques sur DataFrame")
        print("3 - Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            simple_calculator_interface()
        elif choice == "2":
            # Exemple avec un DataFrame fictif
            data = {
                "Ages": [23, 25, 23, 30, 40, 25],
                "Scores": [80, 90, 80, 70, 60, 90]
            }
            df = pd.DataFrame(data)
            print("\nColonnes disponibles :", df.columns.tolist())
            col = input("Choisissez une colonne : ")
            if col in df.columns:
                print("Moyenne :", mean(df, col))
                print("Médiane :", median(df, col))
                print("Mode :", mode(df, col))
                print("Max :", maximum(df, col))
                print("Min :", minimum(df, col))
            else:
                print("Colonne invalide.")
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()