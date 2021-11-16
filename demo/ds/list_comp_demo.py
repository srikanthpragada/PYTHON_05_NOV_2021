st = "Python"

codes = []
for c in st:
    codes.append(ord(c))

print(codes)

codes = [ord(c) for c in st]
codes = [ord(c) for c in st if c.islower()]
print(codes)
