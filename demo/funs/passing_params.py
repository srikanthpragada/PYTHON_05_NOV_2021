def increment(n):
    print(id(n))
    n = n + 1
    print(id(n))
    print(n)


def prepend(lst, value):
    print(id(l))
    lst.insert(0, value)


# Immutable object
a = 100
print(id(a))
increment(a)
print(a)

# Mutable object
l = [10, 20, 30]
print(id(l))
prepend(l, 50)
print(l)
