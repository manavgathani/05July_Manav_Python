# Program to sum of three given integers if two values are equal then sum will be zero.

num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
num3=int(input("Enter number 3 : "))

sum=num1+num2+num3
if num1==num2 or num2==num3 or num1==num3:
    print("Sum is zero")
else:
    print(sum)