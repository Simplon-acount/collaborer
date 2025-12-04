
import pandas as pd

def mean(df, column):
    return df[column].mean()

def median(df, column):
    return df[column].median()

def mode(df, column):
   mode1 = df[column].mode()[0]
   mode2 = df[column].mode()[1]
   return mode1,mode2

def maximum(df, column):
    return df[column].max()

def minimum(df, column):
    return df[column].min()
