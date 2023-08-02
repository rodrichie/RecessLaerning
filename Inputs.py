# Getting multiple inputs

# The map function is used to convert members in a linear data structure into a specific type.

# Using the tuple key word you can convert the map object into a tuple
tup = tuple(map(int, input("Input some numbers...").split()))
print(tup)

#You can also use the list key word to create an array out of a map object.
arr = list(map(int, input("Input some numbers...").split()))
print(arr)

# Destructuring a tuple

# The values obtained can be stored in variables after input.
(a,b,c) = tuple(map(int, input("Input some numbers...").split()))
print(a,b,c)