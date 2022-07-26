# Program to get a single string from two given strings,seperated by a space and swap first two characters of each string.
str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")

x=str1[0:2]

str1=str1.replace(str1[0:2], str2[0:2])

str2=str2.replace(str2[0:2], x)

print("First String has become :",str1)
print("Second String has become :",str2)