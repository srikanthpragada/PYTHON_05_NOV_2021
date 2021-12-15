import os

g = os.walk(r"c:\classroom\nov5p\demo")

count = 0
for (dirname, dirs, files) in g:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
            count += 1

print(f"Count = {count}")
