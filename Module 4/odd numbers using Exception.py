# Python program that user to enter only odd numbers, else will raise an exception.

num=int(input("Enter a number:"))
try:
    mod=num%2
    if mod>0:
        print("This is an odd number")
except Exception as e:
        print(e)