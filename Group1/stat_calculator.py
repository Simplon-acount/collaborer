import pandas as pd

def calculate_mean(df, column):
    try:
        return df[column].mean()
    except Exception as e:
        return f"Erreur lors du calcul de la moyenne : {e}"


def calculate_median(df, column):
    try:
        return df[column].median()
    except Exception as e:
        return f"Erreur lors du calcul de la médiane : {e}"


def calculate_mode(df, column):
    try:
        mode_values = df[column].mode()
        return mode_values.tolist()
    except Exception as e:
        return f"Erreur lors du calcul du mode : {e}"


def calculate_max(df, column):
    try:
        return df[column].max()
    except Exception as e:
        return f"Erreur lors du calcul du maximum : {e}"


def calculate_min(df, column):
    try:
        return df[column].min()
    except Exception as e:
        return f"Erreur lors du calcul du minimum : {e}"
