# Print factors for the all the numbers given on command line

import sys

if len(sys.argv) < 2:
    print("Usage : python allfactors.py <number> ...")
    exit(0)

factors = set()

for arg in sys.argv[1:]:
    num = int(arg)
    for i in range(2, num//2 + 1):
        if num % i == 0:
            factors.add(i)

for n in sorted(factors):
    print(n)
