# Print common factors for the given 2 numbers

num1 = int(input("Enter number :"))
num2 = int(input("Enter number :"))

smallest = num1 if num1 < num2 else num2

for i in range(2, smallest // 2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
