import pandas as pd


# Some fake data:
dat1 = {'a': 'a0 a1 a2 a3'.split(),
        'b': 'b0 b1 b2 b3'.split(),
        'c': 'c0 c1 c2 c3'.split()}

dat2 = {'a': 'a4 a5 a6 a7'.split(),
        'b': 'b4 b5 b6 b7'.split(),
        'c': 'c4 c5 c6 c7'.split()}

dat3 = {'a': 'a8 a9 a10 a11'.split(),
        'b': 'b8 b9 b10 b11'.split(),
        'c': 'c8 c9 c10 c11'.split()}

# Data Frame objects:
df1 = pd.DataFrame(dat1, index=[0, 1, 2, 3])
df2 = pd.DataFrame(dat2, index=[4, 5, 6, 7])
df3 = pd.DataFrame(dat3, index=[8, 9, 10, 11])

# Concatenation. Note: dimension must be in agreement
ccat = pd.concat([df1, df2, df3])  # One big table in result.

# Concatenation along the axis 1:
ccat2 = pd.concat([df1, df2, df3], axis=1)  # Nan in missing data.


# ===================== MERGING ===============================

left = pd.DataFrame({'key': 'k0 k1 k2 k3'.split(),
                     'a': 'a0 a1 a2 a3'.split(),
                     'b': 'b0 b1 b2 b3'.split()})

right = pd.DataFrame({'key': 'k0 k1 k2 k3'.split(),
                     'c': 'c0 c1 c2 c3'.split(),
                     'd': 'd0 d1 d2 d3'.split()})
# Merging
mrgd = pd.merge(left, right, how='inner', on='key')

#print(mrgd)

# ===================== JOINING ================================

left1 = pd.DataFrame({'x': 'x0 x1 x2 x3'.split(),
                     'a': 'a0 a1 a2 a3'.split(),
                     'b': 'b0 b1 b2 b3'.split()},
                     index = 'k l m o'.split())

right1 = pd.DataFrame({'y': 'y0 y1 y2 y3'.split(),
                     'c': 'c0 c1 c2 c3'.split(),
                     'd': 'd0 d1 d2 d3'.split()},
                     index = 'k m l p'.split())

inn = left1.join(right1)
out = left1.join(right1, how='outer')

print(inn)
print(out)
