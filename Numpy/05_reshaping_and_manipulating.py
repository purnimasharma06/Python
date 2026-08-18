# reshaping and manipulating arrays
import numpy as np

# reshaping arrays
# reshape(rows, cols) specify new shape , if dimensions match, it will reshape the array, otherwise it will throw an error

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)  # reshape to 2 rows and 3 columns, it never creates any copy, it returns a new view of the original array with the specified shape
print(reshaped_arr)

# flattening arrays
# flatten() method returns a copy of the array collapsed into one dimension 
# ravel() method returns a flattened one-dimensional array, but it returns a view of the original array whenever possible, which means that modifying the raveled array will also modify the original array.

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.ravel())  # returns a flattened one-dimensional array, but it returns a view of the original array
print(arr_2d.flatten())  # returns a copy of the array collapsed into one dimension