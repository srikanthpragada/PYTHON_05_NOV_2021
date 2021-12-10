class BalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Trying to withdraw {self.amount}, but available balance is {self.balance}"

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
        if amount <= 0:
            raise ValueError(f"Invalid amount {amount}. Valid amount should be > 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"Invalid amount {amount}. Valid amount should be > 0")

        if amount > self.__balance:
            raise BalanceError(self.__balance, amount)

        self.__balance -= amount

    def getbalance(self):
        return self.__balance


# Create object
ac1 = SavingsAccount("101", "Steve")
ac1.deposit(10000)
ac1.withdraw(20000)
ac2 = SavingsAccount("102", "Scott", 10000)
print(ac2.__dict__)
print(ac2._SavingsAccount__balance)
# Call methods
ac1.deposit(5000)
ac1.show()
