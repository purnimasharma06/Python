#  shape
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])


print(arr.shape)  # Output: (2, 3) - 2 rows and 3 columns

# size
print(arr.size)  # Output: 6 - total number of elements in the array

# ndim
print(arr.ndim)  # Output: 2 - number of dimensions of the array

# dtype
print(arr.dtype)  # Output: int64 (or int32 depending on the system, it may be float64 if the array contains floats) - data type of the elements in the array

# Change data type
arr_float = arr.astype(float)
print(arr_float.dtype)  # Output: float64 - data type of the elements in the array

# ------------------------------ MATHEMATICAL OPERATIONS ------------------------------
# Addition Subtraction Multiplication Division and so on
temp = np.array([10, 20, 30])

print(temp + 5) 
print(temp * 2)
print(temp ** 2)


# Aggregation Functions
# sum, mean, min, max, std(standard deviation), var
new_arr = np.array([10, 20, 30, 40, 50])
print(np.sum(new_arr))  # Output: 150
print(np.mean(new_arr))  # Output: 30.0 
print(np.min(new_arr))  # Output: 10
print(np.max(new_arr))  # Output: 50
print(np.std(new_arr))  # Output: 14.142135623730951
print(np.var(new_arr))  # Output: 200.0