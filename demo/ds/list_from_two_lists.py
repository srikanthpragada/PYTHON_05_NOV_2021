l1 = ['a', 'b', 'c', 'd']
l2 = [10, 20, 30]

for idx, value in enumerate(l1):
    if idx < len(l2):
        print(value, l2[idx])
    else:
        print(value, None)
