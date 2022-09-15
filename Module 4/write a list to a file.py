# Python program to write a list to a file.

color=["Red","White","Black","Purple","Orange","Blue","Green","Yellow"]
fl=open("test.txt","w")
for c in color:
    fl.write("%s\n" % c)
content=open("test.txt")
print(content.read())