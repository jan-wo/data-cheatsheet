import numpy as np


py_list_1d = [1, 2, 3]
py_list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Convert python obj to numpy array
arr = np.array(py_list_2d)

# Generate range of numbers with step controll. Also for floats!
arang = np.arange(0.1, 11.9, 2.5)

# Zeros array 5 x 5:
zeros = np.zeros((5, 5))  # note: put tuple as argument!

# Linspace -- similar to arange but third argument is a number of points:
linspace = np.linspace(0, 10, 11)

# Identity matrix:
ident = np.eye(10)

# Random numbers from uniform distribution:
rands = np.random.rand(3, 3)

# Random numbers from normal distribution:
nrands = np.random.randn(5, 5)

# Random integers between 1 and 99:
intrands = np.random.randint(1, 100, 10)

# Print:
#print(intrands)

# --------------------------  Methods on arrays   ----------------------------

# test data:
vect_a = np.random.randint(0, 50, 9)

# Reshape vector to an array:
reshaped = vect_a.reshape(3, 3)

# Maximum/Minimum value in the array:
max = vect_a.max()

# Index of max value (counting from 0):
ind_max = vect_a.argmax()

# Shape of the data:
shp = vect_a.shape

# Data type in the array:
dtyp = vect_a.dtype

# Overwrite sliced values:
# Important note: NUMPY SLICING DO NOT COPY AN ARRAY!
# there is method copy for copying arrays
overwritten_slice = vect_a.copy()
overwritten_slice[0:3] = 100

# Conditional selection:
cpy_vector = vect_a.copy()
biggers_25 = cpy_vector[cpy_vector > 25]


# ----------------------    Array operations:    -----------------------------

# Examplar array [0 1 2 ... 10]
arr = np.arange(0,11)

# Arithmetic (working on elements):
arr_sum = arr + arr
arr_multi = arr * arr
arr_scalar = arr * 100
arr_expo = arr**8

# Numpy dont't error if error with one element:
warning_operation = arr / arr



print(vect_a)
print(biggers_25)
