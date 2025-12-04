# stat_calculator.py
import pandas as pd
import numpy as np

# 6. Normalisation
def normalise(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    df_norm = df.copy()
    for col in numeric_cols:
        min_val = df[col].min()
        max_val = df[col].max()
        if max_val != min_val:
            df_norm[col] = (df[col] - min_val) / (max_val - min_val)
        else:
            df_norm[col] = 0
    return df_norm

# 7. Mode et modulo
def mod(df1, df2, modulo=2):
    mode_df1 = df1.mode().iloc[0]
    numeric_cols_df2 = df2.select_dtypes(include=np.number).columns
    modulo_df2 = df2[numeric_cols_df2] % modulo
    return mode_df1, modulo_df2

# 8. Moyenne et médiane
def averageMed(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    mean = df[numeric_cols].mean()
    median = df[numeric_cols].median()
    return mean, median

def moreDispersed(df1, df2):
    norm_df1 = normalise(df1)
    norm_df2 = normalise(df2)
    std1 = norm_df1.select_dtypes(include=np.number).std().mean()
    std2 = norm_df2.select_dtypes(include=np.number).std().mean()
    if std1 > std2:
        return "df1 est plus dispersé"
    elif std2 > std1:
        return "df2 est plus dispersé"
    else:
        return "Les deux DataFrames ont la même dispersion"

def maxMin(numbers):
    return max(numbers), min(numbers)

def dfStats(df1, df2):
    norm1 = normalise(df1)
    norm2 = normalise(df2)
    mode1, mod2 = mod(df1, df2)
    mean1, median1 = averageMed(df1)
    dispersion = moreDispersed(df1, df2)

    return {
        "normalise_df1": norm1,
        "normalise_df2": norm2,
        "mode_df1": mode1,
        "modulo_df2": mod2,
        "mean_df1": mean1,
        "median_df1": median1,
        "dispersion": dispersion
    }
import pandas as pd

def mean(df, column):
    return df[column].mean()

def median(df, column):
    return df[column].median()

def mode(df, column):
    return df[column].mode().tolist()  # retourne une liste (plusieurs modes possibles)

def maximum(df, column):
    return df[column].max()

def minimum(df, column):
    return df[column].min()
