class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property    # getter
    def hour(self):
        return self.h

    @hour.setter  # setter
    def hour(self, value):
        if value >= 0 and value <= 23:
            self.h = value
        else:
            raise ValueError("Invalid Time")

    @property
    def totalseconds(self):
        return t.h * 3600 + t.m * 60 + t.s


t = Time(10, 20)
t.hour = 30
print(t.hour, t.totalseconds)  # Property
