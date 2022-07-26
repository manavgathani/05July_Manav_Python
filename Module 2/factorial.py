# Program to print a factorial of a number
num=int((input("Enter a number:")))
factorial=1

if num<0:
    print("Factorial of a negative number does not exist")
elif num==0:
    print("The Factorial of a number 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of", num, "is", factorial)