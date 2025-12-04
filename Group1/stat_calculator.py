import pandas as pd
import numpy as np
from scipy import stats

# 6. Normalise un DataFrame (min-max scaling)
def normalise(df):
    """Retourne le DataFrame normalisé avec Min-Max scaling (valeurs entre 0 et 1)."""
    return (df - df.min()) / (df.max() - df.min())

# 7. Mode de deux DataFrames (colonnes numériques uniquement)
def mod(df1, df2):
    """Retourne le mode de df1 et le mode de df2 (pour chaque colonne numérique)."""
    mode1 = df1.mode(numeric_only=True).iloc[0]  # Prend le premier mode si plusieurs
    mode2 = df2.mode(numeric_only=True).iloc[0]
    return mode1, mode2

# 8. Moyenne et médiane
def averageMed(df):
    """Retourne la moyenne et la médiane (pour chaque colonne numérique)."""
    mean_vals = df.mean(numeric_only=True)
    median_vals = df.median(numeric_only=True)
    return mean_vals, median_vals

# 9. Lequel est le plus dispersé (après normalisation)
def moreDispersed(df1, df2):
    """Compare la dispersion (écart-type) après normalisation. Retourne 'df1', 'df2' ou 'égal'."""
    norm1 = normalise(df1.select_dtypes(include=np.number))
    norm2 = normalise(df2.select_dtypes(include=np.number))
    
    std1 = norm1.std().mean()  # Moyenne des écarts-types des colonnes
    std2 = norm2.std().mean()
    
    if std1 > std2:
        return "df1"
    elif std2 > std1:
        return "df2"
    else:
        return "égal"

# 10. Max et min d'une liste
def maxMin(numbers):
    """Retourne (max, min) d'une liste de nombres."""
    if not numbers:
        raise ValueError("La liste est vide.")
    return max(numbers), min(numbers)

# 11. Fonction combinée : dfStats
def dfStats(df1, df2, numbers):
    """Fonction avancée combinant les fonctions 6 à 10."""
    # 6
    norm1 = normalise(df1.select_dtypes(include=np.number))
    norm2 = normalise(df2.select_dtypes(include=np.number))
    
    # 7
    mode1, mode2 = mod(df1, df2)
    
    # 8
    mean1, median1 = averageMed(df1)
    mean2, median2 = averageMed(df2)
    
    # 9
    more_disp = moreDispersed(df1, df2)
    
    # 10
    maxi, mini = maxMin(numbers)
    
    return {
        "normalised_df1": norm1,
        "normalised_df2": norm2,
        "mode_df1": mode1,
        "mode_df2": mode2,
        "mean_df1": mean1,
        "median_df1": median1,
        "mean_df2": mean2,
        "median_df2": median2,
        "more_dispersed": more_disp,
        "max_value": maxi,
        "min_value": mini
    }
