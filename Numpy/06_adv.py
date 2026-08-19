# ----------------------------------- ADVANCE PART OF NUMPY ----------------------------------- 
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
# Insert - np.insert(arr, index, value, axis=None) if axis = 0 row-wise , axis = 1 col wise , none - flatten version 
new_arr = np.insert(arr, 2, 100, axis=0) # Insert 100 at index 2
print(new_arr)

# insert in 2d 
arr_2d = np.array([[1, 2], [3, 4]])
new_arr_2d = np.insert(arr_2d, 1, [5, 6], axis=0) # Insert [5, 6] at index 1 row-wise
print(new_arr_2d)

# append at the end - np.append(arr, value, axis=None) if axis = 0 row-wise , axis = 1 col wise , none - flatten version
new_arr = np.append(arr, 100) # Append 100 at the end
print(new_arr)

# concatenate - np.concatenate((arr1, arr2), axis=0) if axis = 0 row-wise vertical stacking , axis = 1 col wise horizontal stacking, none - flatten version
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
new_arr_c = np.concatenate((arr1, arr2), axis=0) # Concatenate arr1 and arr2 row-wise
print(new_arr_c)

# removing elements of array - np.delete(arr, index, axis=None) if axis = 0 row-wise , axis = 1 col wise , none - flatten version
new_arr_d = np.delete(arr, 0) # Delete element at index 0
print(new_arr_d)

# remove elements in 2d
arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) 
new_arr_2d_d = np.delete(arr_2d, 0, axis=0) # Delete row at index 0
print("Remove row from 2d")
print(new_arr_2d_d)

# stacking - np.vstack((arr1, arr2)) vertical stacking , np.hstack((arr1, arr2)) horizontal stacking
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
new_arr_v = np.vstack((arr1, arr2)) # Stack arr1 and arr2 vertically
print(new_arr_v)
new_arr_h = np.hstack((arr1, arr2)) # Stack arr1 and arr2 horizontally
print(new_arr_h)


# splitting - np.split(arr, indices_or_sections, axis=0) if axis = 0 row-wise , axis = 1 col wise , none - flatten version
# np.split(arr, 2) # Split arr into 2 equal parts
# np.hsplit(arr, 2) # Split arr into 2 equal parts horizontally
# np.vsplit(arr, 2) # Split arr into 2 equal parts vertically
temp = np.array([10, 20, 30, 40, 50, 60])
new_arr_s = np.split(temp, 2) # Split temp into 2 equal parts
print(new_arr_s)
