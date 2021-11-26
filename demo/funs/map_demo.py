def gettype(n):
    return 'Big' if len(n) > 5 else 'Small'


names = ["Bill", "Richards", "Roberts", "Mark", 'scott']

for l in map(len, names):
    print(l)

for n in map(str.upper, names):
    print(n)

for l in map(gettype, names):
    print(l)
