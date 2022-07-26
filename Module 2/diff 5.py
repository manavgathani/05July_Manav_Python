# Program that will return true if the two given integer value are equal or their sum or diff is 5
num1=int(input("Enter a number 1 : "))
num2=int(input("Enter a number 2 : "))

if num1==num2 or num1-num2==5:
    print("True")
else:
    print("False")