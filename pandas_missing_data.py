"""

This is small tutorial about what to do with the missing data.

"""
import pandas as pd
import numpy as np

# Fake data with missing values
data = {'a': [1, 2, np.nan], 'b': [4, np.nan, np.nan], 'c': [3, 2, 1]}

# Data frame:
df = pd.DataFrame(data)

# ------------------------   Dropping rows/columns   --------------------------

# Discard rows/columns containing insufficient data:
dis_1 = df.dropna()         # Drop columns and rows.
dis_2 = df.dropna(axis=1)   # Drop all axis=1 (columns) with missing data set.

# Set treshold: minimal number of data entries to keep row/column:
dis_3 = df.dropna(axis=0, thresh=2)


# ------------------------  Filling empty spaces   ----------------------------

# Filling with some entry given a priori:
fill_1 =df.fillna(value='CUSTOM FILLING')

# Filling with a mean of a given column:
fill_2 = df['a'].fillna(value=df['a'].mean())

print(fill_2)
