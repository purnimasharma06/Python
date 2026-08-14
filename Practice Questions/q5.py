# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))

# Assuming each dog has 4 legs and each chicken has 2 legs
# Let d = number of dogs, c = number of chickens
# d + c = total_heads
# 4d + 2c = total_legs

# Solving the system of equations
d = (total_legs - 2 * total_heads) // 2
c = total_heads - d

print("Number of dogs:", d)
print("Number of chickens:", c)