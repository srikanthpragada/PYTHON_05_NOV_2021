l1 = ['a', 'b', 'c', 'd']
l2 = [10, 20, 30, 40]

ll = l1 if len(l1) >= len(l2) else l2
sl = l1 if len(l1) < len(l2) else l2

for idx, value in enumerate(ll):
    if idx < len(sl):
        print(value, sl[idx])
    else:
        print(value, None)
