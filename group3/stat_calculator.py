import pandas as pd

# Normalisation
def normalise(df: pd.DataFrame):
    # On évite la division par zéro si max == min
    if (df.max() - df.min()).any() == 0:
        return df 
    return (df - df.min()) / (df.max() - df.min())

# Calcul du mode et du modulo
def mod(df1, df2):
    # Le mode (la valeur la plus fréquente) de df1
    mode_df1 = df1.mode()
    
    # Le modulo (reste de la division)
    modulo_res = df1 % df2
    
    return mode_df1, modulo_res

