class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __lt__(self, other):
        return self.age < other.age


people = [Person("A", 20), Person("C", 40), Person("B", 15), Person("E", 19)]

for p in sorted(people):
    print(p)
