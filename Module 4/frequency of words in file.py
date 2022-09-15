# Python program to count the frequency of words in a file.

from collections import Counter
def word_count(filename):
    with open(filename) as fl:
        return Counter(fl.read().split())
print("Number of words in a file:",word_count("test.txt"))