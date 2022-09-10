# A set is a collection of values
# Values in a set are not ordered
# Values in a set are not indexed
# we can add values to set but can't change existing values

fruits = {"grapes","apples","berries"}
# loop through set
for x in fruits:
    print(x)

# Creating set using a Constructor
animals = (("lion","tiger","bear"))
print(animals)
# print length of set
print(len(animals))

# Built in set Methods add, update, clear, discard, remove, del
fruits.add("oranges")
print(fruits)

fruits.update(["mango","kiwi"])
print(fruits)

fruits.remove("kiwi")
print(fruits)

# clear the set
fruits.clear()
# returns empty set
print(fruits)

# delete the set
del animals
