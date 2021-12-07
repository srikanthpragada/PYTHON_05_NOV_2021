class Student:
    courses = {'java': 10000, 'python': 8000, '.net': 12000}

    # Constructor
    def __init__(self, name, course):
        if course not in Student.courses:
            raise ValueError("Invalid course!")

        # object attributes
        self.name = name
        self.course = course
        self.feepaid = 0

    # Methods
    @property
    def totalfee(self):
        return Student.courses[self.course]

    @property
    def dueamount(self):
        return  self.totalfee - self.feepaid

    def show(self):
        print(f"Name     : {self.name}")
        print(f"Course   : {self.course}")
        print(f"Fee paid : {self.feepaid}")

    def payment(self, amount):
        if amount > self.dueamount:
            raise ValueError(f"Excess fee being paid! Due amount is {self.dueamount}, but {amount} is being paid")

        self.feepaid += amount

    def __str__(self):
        return f"{self.name} - {self.course} - {self.feepaid}"

    def __eq__(self, other):
        # print("__eq__")
        return self.name == other.name and self.course == other.course

    def __gt__(self, other):
        return self.feepaid > other.feepaid

    def __add__(self, amount):
        obj = Student(self.name, self.course)
        obj.feepaid = self.feepaid + amount
        return obj


# Create object of Student class


s1 = Student("Stephen", "java")
s2 = Student("Stephen", "java")
s1.payment(5000)
s1.payment(10000)
print(s1.dueamount)

print(s1 == s2)  # s1.__eq__(s2)
print(s1 != s2)
print(s1 > s2)  # s1.__gt__(s2)
s3 = s1 + 10000  # s1.__add__(10000)
print(s1)
print(s3)

# Call methods
s1.payment(5000)
s1.show()
print(s1)
print(str(s1))
print(s1.__str__())
