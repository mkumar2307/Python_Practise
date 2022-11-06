#To Create a dictionary containing key, value pairs of first 12 values of fibonacci

n = 12
a = 0
b = 1

d = dict()
for i in range(1,n+1):
    d[i] = a
    a,b = b,a+b
print(d)