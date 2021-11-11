# Print factorial for the given number

num = int(input("Enter number :"))

fact = 1
for i in range(2, num + 1):
    fact = fact * i

print(f"Factorial of {num} is {fact}")


