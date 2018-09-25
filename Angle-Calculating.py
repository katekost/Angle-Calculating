import pandas as pd
import numpy as np
import math

df = pd.read_csv("aprox.csv", sep=';')
df['derivative'] = np.nan
df['h'] = np.nan
df['arctg_rad'] = np.nan
df['degrees'] = np.nan

for i in range(0, df.shape[0]-1):
    df.iloc[i, 3] = df.iloc[i+1, 0] - df.iloc[i, 0]

two_h = 2*max(df.h)

for i in range(0, df.shape[0]-1):
    df.iloc[i, 2] = (df.iloc[i+1, 0] - df.iloc[i, 0])/(two_h)

for i in range(0, df.shape[0]-1):
    df.iloc[i, 4] = math.atan(df.iloc[i, 2])

for i in range(0, df.shape[0]-1):
    df.iloc[i, 5] = math.degrees(df.iloc[i, 4])
