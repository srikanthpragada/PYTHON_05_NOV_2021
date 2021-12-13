# Marks list

f = open("marks.txt", "rt")

students = {}
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    name = parts[0]

    # Take only numbers from parts
    valid_marks = filter(str.isdigit, parts[1:])

    # Convert all strings to int
    marks = list(map(int, valid_marks))
    count = len(marks)
    total = sum(marks)
    students[name] = (total, total // count)

f.close()

for name, details in sorted(students.items()):
    print(f'{name:20} {details[0]:5} {details[1]:5}')
