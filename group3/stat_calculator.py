import pandas as pd

# 6. Normalisation
def normalise(df: pd.DataFrame):
    # Évite division par zéro colonne par colonne
    return (df - df.min()) / (df.max() - df.min()).replace(0, 1)


# 7. Mode
def mod(df1: pd.DataFrame, df2: pd.DataFrame):
    return df1.mode(), df2.mode()


# 8. Moyenne et médiane
def averageMed(df: pd.DataFrame):
    avg = df.mean()
    med = df.median()
    return avg, med


# 9. Dispersions après normalisation
def moreDispersed(df1: pd.DataFrame, df2: pd.DataFrame):
    n1 = normalise(df1)
    n2 = normalise(df2)

    disp1 = n1.std().mean()
    disp2 = n2.std().mean()

    if disp1 > disp2:
        return "df1 est plus dispersé"
    elif disp2 > disp1:
        return "df2 est plus dispersé"
    else:
        return "Les deux DataFrames ont la même dispersion"


# 10. Maximum et minimum d'une liste
def maxMin(numbers: list):
    if not numbers:
        return None, None
    return max(numbers), min(numbers)


# 11. dfStats : fonction combinée
def dfStats(df1: pd.DataFrame, df2: pd.DataFrame):
    # Normalisation
    df1_norm = normalise(df1)
    df2_norm = normalise(df2)

    # Mode
    mode1, mode2 = mod(df1, df2)

    # Moyenne / médiane
    avg1, med1 = averageMed(df1)
    avg2, med2 = averageMed(df2)

    # Dispersion
    dispersion = moreDispersed(df1, df2)

    return {
        "df1_normalized": df1_norm,
        "df2_normalized": df2_norm,
        "mode_df1": mode1,
        "mode_df2": mode2,
        "average_df1": avg1,
        "median_df1": med1,
        "average_df2": avg2,
        "median_df2": med2,
        "more_dispersed": dispersion
    }