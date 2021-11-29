d = {1: 10, 3: 5, 2: 20, 5: 1}

for n in sorted(d.items(), key=lambda t: t[1]):
    print(n)
