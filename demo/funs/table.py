def table(num, length=10):
    for n in range(1, length + 1):
        print(f"{num:3} * {n:2} = {num * n:5}")


# table(15)
# table(25, 5)

num = int(input("Enter number :"))
length = input("Enter length :")
if length == '':
    table(num)
else:
    table(num, int(length))
