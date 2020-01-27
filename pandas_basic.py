import pandas as pd
import numpy as np
from numpy.random import randn

labels = ['a', 'b', 'c']
dat = [10, 20, 30]
arr = np.array(dat)
dic = {'a': 10, 'b': 20, 'c':30}


# Pandas series can be build on literally anything:
ser = pd.Series(data=dat, index=labels)
ser = pd.Series(data=arr, index=labels)
ser = pd.Series(dic)

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'GB', 'RU', 'PL'])
ser2 = pd.Series([1, 2, 3, 4], ['GB', 'USA', 'PL', 'TT'])

# Adding series is matched asing on labels. Not mached -> NaN
ser3 = ser1 +ser2

# Data frames
# DF is just a bunch of Series sharing the same label.
np.random.seed(101)  # For consistent results

df = pd.DataFrame(randn(5,4), ['a', 'b', 'c', 'd', 'e'], ['w', 'x', 'y', 'z'])
w_and_z = df[['w', 'z']]

# Derive new column from already existing:
df['new'] = df['x'] + df['y']

# Remove column:
drp = df.drop('a', axis=0)  # axis = 0: rows, = 1: columns
drp = drp.drop('new', axis=1)

# Remove 'In place':
drp.drop('z', axis=1, inplace=True)

# Selecting rows by label
rw = df.loc['a']  # Note: it is going to be displayed in column.

# Selecting rows by numeric index:
rw2 = df.iloc[2]

# Selecting crossection:
cs1 = df.loc['b', 'y']  # Single number
cs2 = df.loc[['a', 'b'], ['w', 'y']]

print(cs2)
