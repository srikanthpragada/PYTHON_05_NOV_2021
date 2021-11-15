numbers = []  # Empty list

while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    numbers.append(num)

# Display list in sorted order
for n in sorted(numbers):
    print(n)
