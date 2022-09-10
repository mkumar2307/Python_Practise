# tuple is a list that can not be changed (immutable)
fruits = ("grapes","apples","berries")

# loop through tuple using a for loop
for x in fruits:
    print(x)

# accesing elements in tuple by using index numbers
print(fruits[2])

# tuple using a tuple constructor
animals = tuple(("lion","tiger","bear"))
print(animals)

# print length of elements tuple
print(len(animals))

# delete tuple
del animals