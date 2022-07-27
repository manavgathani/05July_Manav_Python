# Program to return the length of the longest word from the list of words

mylist=[]

n=(input("Enter a list elements :"))


longest=0

for word in n.split():
    if len(word)>longest:
        longest=len(word)
        longest_word=word
print("The longest word is ", longest_word, "with length",len(longest_word))



