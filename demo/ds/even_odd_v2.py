enums = []
onums = []
while True:
    num = int(input("Enter number [ 0 to stop ] :"))
    if num == 0:
        break

    if num % 2 == 0:
        enums.append(num)
    else:
        onums.append(num)

for n in enums + onums:
    print(n)
