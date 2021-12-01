import sys

sys.path.insert(0, r"c:\classroom\nov5p\demo\stlib")
print(sys.path)

import number_functions as nf
from number_functions import isprime

print(nf.iseven(10), isprime(11))
