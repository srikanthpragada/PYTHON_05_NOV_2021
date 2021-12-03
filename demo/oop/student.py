class Student:
    # Constructor
    def __init__(self, name, course):
        # object attributes
        self.name = name
        self.course = course
        self.feepaid = 0

    # Methods
    def show(self):
        print(f"Name     : {self.name}")
        print(f"Course   : {self.course}")
        print(f"Fee paid : {self.feepaid}")

    def payment(self, amount):
        self.feepaid += amount

    def __str__(self):
        return f"{self.name} - {self.course} - {self.feepaid}"

    def __eq__(self, other):
        #print("__eq__")
        return self.name == other.name and self.course == other.course

# Create object of Student class
s1 = Student("Stephen", "Java")
s2 = Student("Stephen", "Java")
print(s1 == s2)   #  s1.__eq__(s2)
print(s1 != s2)


# Call methods
s1.payment(5000)
s1.show()
print(s1)
print(str(s1))
print(s1.__str__())
