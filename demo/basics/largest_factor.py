# Print largest factor for the given number

num = int(input("Enter number :"))

for i in range(num // 2, 0, -1):
    if num % i == 0:
        print(i)
        break


