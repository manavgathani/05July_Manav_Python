# Python program to read first n lines of a file.

n=int(input("Enter Number of lines to read?"))
fl=open("test.txt","r+")
for i in range(n):
    print(fl.readline())