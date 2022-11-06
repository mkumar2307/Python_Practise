n = 100

evens = []
odds = []

for i in range(n+1):
    if not i % 2:
        evens.append(i)
    else:
        odds.append(i)

print(f'The evens are {evens}')
print(f'The odds are {odds}')