
nums = []
while True:
    num = int(input("Enter number [ 0 to stop ] :"))
    if num == 0:
        break

    nums.append(num)

for n in nums:
    if n % 2 == 0:
        print(n)

# Odd numbers
for n in nums:
    if n % 2 == 1:
        print(n)