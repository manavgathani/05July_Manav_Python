# Program to count the number of characters in a string.
string= input("Enter the string: ")
count=0

for i in range(0,len(string)):
    if(string[i]!=""):
        count=count+1
print("Total number of Characters in a string:",str(count))