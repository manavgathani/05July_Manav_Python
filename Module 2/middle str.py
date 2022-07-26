# Program to insert a string in a middle of a string.

# Using Split() Function

mystr="What are doing?"
split=mystr.split()
split.insert(2, "you")
final=" ".join(split)
print(final)