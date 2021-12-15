import os
import sys


def file_contains(filename, searchstring) -> bool:
    with open(filename, "rt") as f:
        return searchstring in f.read()


if len(sys.argv) < 2:
    print("Usage : python search_python_files.py  <searchstring>")
    exit(0)

g = os.walk(r"c:\classroom\nov5p\demo")
searchstring = sys.argv[1]  # Search string

for (dirname, dirs, files) in g:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f  # Absolute path
            if file_contains(filename, searchstring):
                print(filename)
