# Python program to count the number of lines in a text file.

def file_length(filename):
    with open(filename) as fl:
        for i,l in enumerate(fl):
            pass
    return i+1
print("Number of lines in the file:",file_length("test.txt"))