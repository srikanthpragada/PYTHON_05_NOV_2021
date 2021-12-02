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


# Create object of Student class
s1 = Student("Stephen", "Java")
# Call methods
s1.payment(5000)
s1.show()