# Write a program to find the euclidean distance between two coordinates.
a = float(input("Enter the x-coordinate of the first point: "))
b = float(input("Enter the y-coordinate of the first point: "))
c = float(input("Enter the x-coordinate of the second point: "))
d = float(input("Enter the y-coordinate of the second point: "))

distance = ((c - a)**2 + (d - b)**2) ** 0.5
print("The Euclidean distance between the two points is:", distance)
