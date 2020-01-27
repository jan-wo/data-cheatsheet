import pandas as pd
import numpy as np
from numpy.random import randn

# Some dummy data:
np.random.seed(101)
outer = "o1 o1 o1 o2 o2 o2".split()  # Outer indexes.
inner = "i1 i2 i3 i1 i2 i3".split()  # Inner indexes.
hier_ind = list(zip(outer, inner))   # list of tuples.
hier_ind = pd.MultiIndex.from_tuples(hier_ind)  # Index hierarchy.

# Multi-index data frame:
df = pd.DataFrame(randn(6,2), hier_ind, ['a', 'b'])

# Select first outer index data:
o1 = df.loc['o1']

# Go deeper...
o1i1 = df.loc['o1'].loc['i1']  # Note: a row displayed as it was column.

# Naming indexes:
ind_nam = df.index.names              # Show names.
df.index.names = ['outer', 'inner']   # Set new names.

# Pick o2 i2 from column b:
selection = df.loc['o2'].loc['i2'].loc['b']

# Crossection:
cs = df.xs('i1', level='inner')


print(cs)
