class Circle:
    # Class attribute or Static attribute
    PI = 3.14

    # methods
    def __init__(self, x, y, r):
        # Object attribute
        self.x = x
        self.y = y
        self.radius = r

    def area(self):
        return Circle.PI * self.radius * self.radius

    def perimeter(self):
        return 2 * Circle.PI * self.radius

    def __str__(self):
        return f"X = {self.x}, Y = {self.y}, Radius = {self.radius}"

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius


c1 = Circle(10, 20, 6.0)
c2 = Circle(1, 2, 4)

print(c1.area())
print(c2.perimeter())
print(c2)
print(c1 == c2)
print(c1 > c2)
