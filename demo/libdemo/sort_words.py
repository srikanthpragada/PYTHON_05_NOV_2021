import re

with open(r"c:\classroom\nov5p\old_man.txt", "rt") as f:
    words = re.findall(r"\w+", f.read())

for w in sorted(set(words)):
    print(w)
