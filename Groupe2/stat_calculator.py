import pandas as pd

def mean(df, column):
    return df[column].mean()

def median(df, column):
    return df[column].median()

def mode(df, column):
    return df[column].mode().tolist()  # retourne une liste (plusieurs modes possibles)