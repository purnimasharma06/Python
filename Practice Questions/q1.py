# User will input (3ages).Find the oldest one\

age1 = int(input("Enter the first age "))
age2 = int(input("Enter the second age "))
age3 = int(input("Enter the third age "))


if age1 > age2 and age1 > age3:
    print("The oldest age is", age1)
elif age2 > age1 and age2 > age3:   
    print("The oldest age is", age2)
else:
    print("The oldest age is", age3) 
          