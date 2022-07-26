# Program to reverse a string if the length of string is multiple of 4.
mystr=input("Enter a string : ")
length = len(mystr)
print("The length of a string is ",length)
if length % 4==0:
    print("The string is reversed :",mystr[::-1])
else:
    print("The string is not reversed")  