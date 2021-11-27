names = ["Bill", "Richards", "Roberts", "Mark", 'scott']

for n in filter(lambda n: len(n) > 5, names):
    print(n)
