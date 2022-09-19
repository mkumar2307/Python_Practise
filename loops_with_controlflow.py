fruits = ["grapes","berries","oranges"]

for x in fruits:
    print(x)
    if x == "berries":
        break

for x in fruits:
    if x == "berries":
        continue
    print(x)

# Range function generate a random integer numbers between given start integer and to the stop integer
for x in range(8):
    print(x)
else:
    print("Loop is over. Bye!")
