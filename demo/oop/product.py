class Product:
    # class attribute or static attribute
    taxrate = 18

    @staticmethod
    def settaxrate(newrate):
        Product.taxrate = newrate

    def __init__(self, name, price):
        # Object attributes
        self.name = name
        self.price = price

    def getnetprice(self):
        return self.price + (self.price * Product.taxrate / 100)



p1 = Product("Product1", 10000)
print(p1.getnetprice())
Product.settaxrate(20)    # Static method
print(p1.getnetprice())

