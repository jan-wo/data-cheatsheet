import pandas as pd
import numpy as np

# Example data
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [100, 300, 200, 300],
                   'col3': 'aaa bbb ccc ddd'.split()})


# Finding unique values:
uniq = df['col2'].unique()

# Number of unique values:
nuniq = df['col2'].nunique()

# Count occurences of every unique value:
cnt = df['col2'].value_counts()

# Apply method:
def times_2(value):
    """
    This can be any function
    """
    return value*2

func_appl = df['col2'].apply(times_2)

# Apply with built-in function:
col_len = df['col3'].apply(len)

# Lambdas also work:
lambda_times = df['col2'].apply(lambda x: x*2)

# Get list of columns / indexes:
clns = df.columns
indx = df.index

# Sorting:
srt1 = df.sort_values(by='col2')

# Showing null values:
nls = df.isnull()

# ---------------------------------------------------------------------

# Pivot table:
data2 = {'A': 'foo foo foo bar bar bar'.split(),
        'B': 'first first second second first first'.split(),
        'C': 'k l k l k l'.split(),
        'D': [4, 3, 4, 2, 2, 1]}

df2 = pd.DataFrame(data2)

pvt = df2.pivot_table(values='D', index=['A', 'B'], columns=['C'])

print(pvt)
