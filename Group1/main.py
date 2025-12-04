# 12. Importer toutes les fonctions
from simple_calculator import add, mean, moyen, multiply, divide
from stat_calculator import normalise, mod, averageMed, moreDispersed, maxMin, dfStats
import pandas as pd

def super_calculateur():
    print("🌟 Bienvenue dans le Super-Calculateur ! 🌟\n")

    # --- Partie 1 : Calculs simples ---
    print("🔢 Calculs simples :")
    a = float(input("Entrez le premier nombre (a) : "))
    b = float(input("Entrez le second nombre (b) : "))
    
    print(f"add({a}, {b}) = {add(a, b)}")
    print(f"mean({a}, {b}) = {mean(a, b)}")
    print(f"moyen({a}, {b}) = {moyen(a, b)}")
    print(f"multiply({a}, {b}) = {multiply(int(a), int(b))} (entiers uniquement)")
    print(f"divide({a}, {b}) = {divide(a, b)}")
    print()

    # --- Partie 2 : Statistiques ---
    print("📊 Statistiques sur deux DataFrames :")
    
    # Créer deux petits DataFrames de démonstration (ou charger des fichiers CSV)
    data1 = {
        "X": [1, 2, 3, 4, 5],
        "Y": [10, 20, 30, 40, 50]
    }
    data2 = {
        "X": [2, 4, 6, 8, 10],
        "Y": [15, 25, 35, 45, 55]
    }
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    numbers = [10, 3, 7, 15, 2, 9]  # liste pour maxMin

    # 11. Appel de dfStats
    stats_result = dfStats(df1, df2, numbers)

    print("\n📈 Résultats statistiques :")
    print("- Modes :")
    print("  df1 :", stats_result["mode_df1"].to_dict())
    print("  df2 :", stats_result["mode_df2"].to_dict())

    print("\n- Moyennes :")
    print("  df1 :", stats_result["mean_df1"].to_dict())
    print("  df2 :", stats_result["mean_df2"].to_dict())

    print("\n- Médianes :")
    print("  df1 :", stats_result["median_df1"].to_dict())
    print("  df2 :", stats_result["median_df2"].to_dict())

    print(f"\n- Le DataFrame le plus dispersé (après normalisation) : {stats_result['more_dispersed']}")

    print(f"\n- Min/Max de la liste {numbers} : min = {stats_result['min_value']}, max = {stats_result['max_value']}")

    print("\n✅ Tous les calculs terminés !")

if __name__ == "__main__":
    super_calculateur()
