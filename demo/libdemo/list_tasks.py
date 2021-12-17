from datetime import *

with open("tasks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(",")
        try:
            sd = datetime.strptime(parts[0], "%d-%m-%Y")
            ed = datetime.strptime(parts[1], "%d-%m-%Y")
            days = (ed - sd).days
            print(f"{parts[2].strip():50} {days:3}")
        except:
            pass
