import pandas as pd

# Normalisation
def normalise(df: pd.DataFrame):
    # On évite la division par zéro si max == min
    if (df.max() - df.min()).any() == 0:
        return df 
    return (df - df.min()) / (df.max() - df.min())

# Calcul du mode
def mod(df1 : pd.DataFrame, df2 : pd.DataFrame):
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