#User will input (2numbers).Write a program to swap the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))  

num3 = num1
num1 = num2
num2 = num3

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)