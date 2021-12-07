from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    @abstractmethod
    def getsalary(self):
        pass


class Consultant(Employee):
    pass


class SalariedEmployee(Employee):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def getsalary(self):
        return self.salary


class OnsiteEmployee(SalariedEmployee):
    def __init__(self, name, dept, salary, allowance):
        super().__init__(name, dept, salary)
        self.allowance = allowance

    def getsalary(self):
        return super().getsalary() + self.allowance


e = SalariedEmployee("Mark", "IT", 800000)
oe = OnsiteEmployee("James", "IT", 1000000, 1000000)
print(e.getsalary())
print(oe.getsalary())
