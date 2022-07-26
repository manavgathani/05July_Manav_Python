# Program that takes a list of words and returns the length of the longest one.

mylist=input("Enter a list :")

longest=0
for words in mylist.split():
    if len(words) > longest:
        longest=len(words)
        longest_word=words

print("The longest word is",longest_word,"with length",len(longest_word))
