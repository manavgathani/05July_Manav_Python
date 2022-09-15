# python program to find the longest words.

def longest_word(filename):
    with open(filename,"r") as fl:
        words=fl.read().split()
    max_len=len(max(words,key=len))
    return [word for word in words if len(word)==max_len]
print(longest_word("test.txt"))