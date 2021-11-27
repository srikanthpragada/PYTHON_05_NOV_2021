data = ["343434", "Richards", "343434", "34343d", '335333']

for l in map(lambda v: v[-1].isdigit(), data):
    print(l)
