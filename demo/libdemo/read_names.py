# Write names into names.txt

f = open("names.txt", "rt")
for name in f.readlines():
    #print(name, end = '')
    print(name.strip())

f.close()