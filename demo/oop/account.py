class SavingsAccount:
    # Constructor
    def __init__(self, acc_number, acc_holder_name, balance=0):
        # object attributes
        self.acc_holder_name = acc_holder_name
        self.acc_number = acc_number
        self.__balance = balance  # Private attribute

    # Methods
    def show(self):
        print(f"Account Number    : {self.acc_number}")
        print(f"Holder's Name     : {self.acc_holder_name}")
        print(f"Balance           : {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def getbalance(self):
        return self.__balance


# Create object
ac1 = SavingsAccount("101", "Steve")
ac2 = SavingsAccount("102", "Scott", 10000)
print(ac2.__dict__)
print(ac2._SavingsAccount__balance)
# Call methods
ac1.deposit(5000)
ac1.show()
