# Python program to read last n lines of a file.

fl=open("test.txt")
lines=fl.readlines()
last_lines=lines[-5:]
print(last_lines)