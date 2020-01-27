import pandas as pd
import numpy as np
from numpy.random import randn

#Some fake random (but consistent) data:
np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['a', 'b', 'c', 'd', 'e'], ['w', 'x', 'y', 'z'])

# Conditional selections
bool_df = df > 0  # Boolean matrix
greater_only = df[bool_df]  # Matrix containing only > 0 elements

# More specific: column containing >0 elements:
greater_only_w = df[df['w'] > 0]  # select rows wich w-column values > 0

# Filter df to show only column 'Y' and 'X' while column w > 0:
wgt0_x = df[df['w']>0][['y', 'x']]


# ------------------------   Multiple conditions   ----------------------------

# Do not use 'and' here as python 'and' operator can work with True/False only.
multi_and = df[(df['w'] > 0) & (df['y'] > 1)]
multi_or = df[(df['w'] > 0) | (df['y'] > 1)]

# ----------------------   Reseting/Setting index   ---------------------------
# While index is reset, old index become a column.
res_ind = df.reset_index()  # Not inplace operation.
# In order to set new indexes, a column have to be created
ind_list = 'au dj ek jj wqw'.split()  # A quick way to create a list.
df['new_ind'] = ind_list  # add
new_ind = df.set_index('new_ind')



#
print(new_ind)
