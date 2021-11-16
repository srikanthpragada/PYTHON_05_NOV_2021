l1 = ['a', 'b', 'c', 'd']
l2 = [10, 20, 30, 40]

for v1, v2 in zip(l1, l2, strict=True):
    print(v1, v2)

for v1, v2 in zip("ABC", "aBc"):
    print(v1, v2)
