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

