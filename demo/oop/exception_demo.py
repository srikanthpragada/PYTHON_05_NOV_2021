try:
    num = int(input("Enter number :"))
    print(100 / num)
except ValueError as ex:
    print("Invalid Number! Error --> ", ex)
except ZeroDivisionError:
    print("Number cannot be zero!")

print("The End")