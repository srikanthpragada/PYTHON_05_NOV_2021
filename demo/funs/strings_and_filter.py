names = ["Bill2", "Richards", "Roberts55", "mark1", 'scott']

for n in filter(lambda s: s[0].isupper() and s[-1].isdigit(), names):
    print(n)
