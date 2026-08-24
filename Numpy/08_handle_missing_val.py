# Handling missing values in numpy
#  built in functions 
# np.isnan(array) - to check if the value is NaN(detect missing values) - returns boolean 

import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan])
print(np.isnan(arr))  # Output: [False False  True False  True] , also the values can be compared directly

# np.nan_to_num(array, nan=value) - to replace NaN with a specified value (default is 0)

temp = np.array([1, 2, np.nan, 4, np.nan])
print(np.nan_to_num(temp, nan=0))  # Output: [1. 2. 0. 4. 0.] - NaN values replaced with 0

# np.isinf(array) - to check if the value is infinite

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr))  # Output: [False False  True False  True False] , also the values can be compared directly

# replace infinite values with a specified value (default is 0)
temp = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.nan_to_num(temp, posinf=1000, neginf=-1000))  # Output: [   1.    2. 1000.    4. -1000.    6.] - infinite values replaced with specified values