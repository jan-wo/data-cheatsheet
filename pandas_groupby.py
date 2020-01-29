import pandas as pd


data = {'State in room': ['gas', 'gas', 'solid', 'solid', 'liquid', 'liquid'],
        'Element': ['Ar', 'He', 'C', 'S', 'Hg', 'Br'],
        'mass': [39, 4, 12, 32, 200, 80]}

df = pd.DataFrame(data)


# group by mass:
by_state = df.groupby('State in room')

mean = by_state.mean()
sum = by_state.sum()
std = by_state.std()

# Pick particular value for a given group:
gas = by_state.sum().loc['gas']

# Count
cnt = df.groupby('State in room').count()

# Describe gives any possible data descriptors:
desc = df.groupby('State in room').describe()

print(desc)
