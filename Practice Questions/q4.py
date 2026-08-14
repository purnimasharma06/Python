#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
num = int(input("Enter a four digit number: "))
ans = ""
while num > 0:
    digit = num % 10
    ans = ans + str(digit)
    num = num // 10

print("The reverse of the number is:", ans)