# Broadcasting - why used?  Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding the smaller array to match the shape of the larger array. This enables efficient vectorized operations without explicitly creating copies of the data.
prices = [100, 200, 300, 400, 500]

discount = 10

final_prices = []
for price in prices:
    final_price = price - (price * discount / 100)
    final_prices.append(final_price)


print(final_prices)  # Output: [90.0, 180.0, 270.0, 360.0, 450.0] - final prices after applying discount

# No need of for loop
# Using broadcasting 
import numpy as np


new_prices = np.array([100, 200, 300])
new_dis = 10
final = new_prices - (new_prices * new_dis / 100)
print(final)  # Output: [90. 180. 270.] - final prices



# How numpy handles arrays of diff shapes 
# 1. Matching dimensions - if the dimensions of the arrays are the same, they can be operated on element-wise.
# 2. Expanding Single Elements - if one of the arrays has a single element, it can be broadcasted to match the shape of the other array.
# 3. Incompatible Shapes - if the dimensions of the arrays are not compatible for broadcasting, NumPy will raise a ValueError.



# How broadcasting will be applied 
# No nedd to access elements one by one using loops



# How to do broadcasting from 1d to 2d arrays 
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30]) 
result = matrix + vector  # Broadcasting will add the vector to each row of the matrix
print(result)  # Output: [[11 22 33] [14 25 36]] - result of adding the vector to each row of the matrix


# When error will come 
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[1, 2]])
# res = arr1 + arr2  # This will raise a ValueError because the shapes are not compatible for broadcasting
# print(res)  #    Output: ValueError: operands could not be broadcast together with shapes (2,3) (1,2)
 

# Vectorization - why used?  Vectorization allows NumPy to perform operations on entire arrays without the need for explicit loops, making the code more concise and efficient.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
ans = [a + b for a, b in zip(list1, list2)]  # Vectorized operation
print(ans)  # Output: [5, 7, 9]

#  fast vectorized approach 
temp1 = np.array([1, 2, 3])
temp2 = np.array([4, 5, 6])
a = temp1 + temp2  # Vectorized operation using NumPy
print(a)  # Output: [5 7 9] - result of adding the two arrays

# fast vectorized approach multiplication
t1 = np.array([10, 20, 30])
mul = t1 * 2  # Vectorized operation using NumPy
print(mul)  # Output: [20 40 60] - result of multiplying



# summary 
#  broadcasting - expands smaller to larger arrays to match , faster than loops
# 1d to 2d -> broadcasting will add the vector to each row of the matrix
# vectorization - 100x faster , opeartions applied on entire array -> matrix operations 