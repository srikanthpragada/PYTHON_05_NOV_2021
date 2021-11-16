# Program to calculate net price

price = float(input("Enter price :"))
discount = price * 15 / 100
gross_price = price - discount
tax = gross_price * 0.05
net_price = gross_price + tax

print(f'Price           : {price:8.2f}')
print(f'-Discount       : {discount:8.2f}')
print(f"                  --------")
print(f'After discount  : {gross_price:8.2f}')
print(f'+Tax            : {tax:8.2f}')
print(f"                  --------")
print(f'Net Price       : {net_price:8.2f}')
