# Program to add 'ing' at the end of the string (length should be atleast 3). If the given string already
# ends with 'ing' then add 'ly' insteadif the string length is less than 3, leave it unchanged.

mystr=input("Enter a string : ")

if len(mystr)<3:
    print("Unchanged",mystr)

if mystr.endswith('ing'):
    mystr+='ly'

elif len(mystr)>=3:
    mystr+='ing'
print(mystr) 