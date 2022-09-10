from audioop import reverse


fruits = ["berries", "apples", "grapes", "orange"]
vegetables = ["kale", "broccoli", "lettuce"]

# adding two lists using extend method
fruits.extend(vegetables)
print(fruits)

# adding new items to list using append method
vegetables.append("beans")
print(vegetables)

# sorting ascending or descending using sort method
vegetables.sort()
print(vegetables)

vegetables.sort(reverse=True)
print(vegetables)

# count method to count no. of occurances
print(fruits.count("berries"))

# index method used to return index positon
print(fruits.index("grapes"))
# add new item to list to any position we want
fruits.insert(0, "banana")
print(fruits)

# pop method to remove items from list
fruits.pop() 
#if none of item names specified last item will be removed
print(fruits)

# remove method to remove specified item from list
vegetables.remove("kale")
print(vegetables)

# del method used to delete a list or remove a item using indexes
del vegetables
