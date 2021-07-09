class Employee:
    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1

    def increase(self):
        self.salary = self.salary * Employee.increment

    @classmethod
    def from_Str(cls, string):
        fname, lname, salary = string.split()
        return cls(fname, lname, int(salary))


class Programmer(Employee):

    def __init__(self, fname, lname, salary, prolang, exp):
        super().__init__(fname, lname, salary)
        self.prolang = prolang
        self.exp = exp

    def increase(self):
        self.salary = self.salary * (Employee.increment+0.2)
        return self.salary

    @classmethod
    def from_Str(cls, string):
        fname, lname, salary, prolang, exp = string.split()
        return cls(fname, lname, int(salary), prolang, int(exp))


print(Programmer('shlok', 'koirala', 5000, 'Python', 1).exp)

print(Programmer.from_Str('shlok koirala 5000 python 1').exp)
