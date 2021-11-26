def isbigname(name):
    return len(name) > 5


def hasupper(name):
    for c in name:
        if c.isupper():
            return True

    return False


names = ["Bill", "Richards", "Roberts", "Mark", 'scott']

for n in filter(isbigname, names):
    print(n)

for n in filter(hasupper, names):
    print(n)
