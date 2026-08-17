# indexing and slicing

# access
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print(arr[0])  # Output: 1 - first element
print(arr[2])  # Output: 3 - third element 
print(arr[-1])  # Output: 5 - last element

# slicing - extracting subset of data 
# arr[start:stop:step]  # elements from index start to stop-1 with a step
print(arr[1:5]) # Output: [2 3 4 5] - elements from index 1 to 4
print(arr[:4]) # Output: [1 2 3 4] - elements from start to index 3
print(arr[::2]) # Output: [1 3 5] - elements from start to end with a step of 2 
print(arr[::-1]) # Output: [5 4 3 2 1] - elements from end to start with a step of -1 (reversing the array)


#  fancy indexing - access multiple elements at once using an array of indices
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[[0, 2, 4]]) # Output: [10 30 50] - elements at index 0, 2 and 4


# filtering data/ boolean masking - access elements based on a condition
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[arr > 30]) # Output: [40 50 60] - elements greater than 30