mystr=input("Enter a string : ")

if len(mystr)<=2:
    print("Empty String")
else:
    newstr=mystr[:2]+mystr[-2:]
    print("New String :",newstr)