# Dictionary is a collection of key value pairs
# Values can be changed (mutable). Values has unique keys

# creating a basic dictionary
mycar = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}

print(mycar)

# creating dictionary using constructor
mygreens = dict(fruit="green apples",vegetables="kale")
print(mygreens)

# Built in dictionar Methods get, update, clear, keys, values, del
print(len(mycar)) # Length of dictionary No. of key value pairs

# updating the values of key's
mycar["year"] = 2019
print(mycar)

# to return value of a key using get method
print(mycar.get("brand"))

# adding new entry to a dictionary
mycar.update({"color": "silver"})
print(mycar)

# keys method used to return list of keys
b = mycar.keys()
print(b)

# values method used to return list of values
b = mycar.values()
print(b)

# remove particular item from dictionary
mycar.pop("color") # we can also use del mycar["color"]
print(mycar)

# clear method clears the dictionary
mycar.clear()
print(mycar)

# del used the delete dictionary
del mycar
