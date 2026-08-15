#  create arrays from python lists 
#  np.array([le1, le2, le3, ...])  # 1D array

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# create arrays with default values
# create arrays with zeros
zeros = np.zeros(5) 
# 5 is the shape/ size of the array
print(zeros)

# create array with ones
ones = np.ones((2,3)) # 2 rows and 3 columns
print(ones)

# full array full(shape, value) with a specific value
full = np.full((3, 4), 7) # 3 rows and 4 columns, filled with 7
print(full)

# creating sequences of numbers in numpy
# arrange(start, stop, step)  # 1D array
arr1 = np.arange(0, 10, 2) # start=0, stop=10, step=2
print(arr1)

# creating identity matrix
identity = np.eye(3) # 3x3 identity matrix
print(identity)

