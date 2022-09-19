# control flow is order in which program's code execute
# conditional statements (if,elif,else) can be used with control flowc
# loops are used to repeat a specific block of code
# function is piece of code that do specific

# if statements used to check conditions before it executes
a = 7
b = 8

if a < b:
    print(a, "is smaller than", b)

# else statements executes if conditions checked evaluates to false
a = 7
b = 8
c = 9

if a > b:
    print(a, " is smaller than", b)
elif b >= c:
    print(b, " is smaller than ", c)
else:
    print(c, "is larger than", b, "and", a)

# while loop statements used to run continuously as long as condition true
i = 1

while i < 7:
    print(i)
    i += 1

# for loop used to iterate over a sequence usally list,tuple,dictionary,set,string
fruits = ["grapes","berries","oranges"]

for x in fruits:
    print(x)

# Nested loop is a loop insdie a loop
colurs = ["green","yellow","purple"]

for x in colurs:
    for y in fruits:
        print(x,y)

# Break is used to terminate the loop
i = 1

while i < 8:
    print(i)
    if i==3:
        break
    i += 1

# continue used to stop current iteration and continue with iteration of loop
i = 0

while i < 8:
    i += 1
    if i==4:
        continue
    print(i)
