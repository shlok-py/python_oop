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
    @classmethod
    def add_increment(cls, amount):
        cls.increment = amount



harry = Employee.from_Str("harry khan 30000")
print(harry.lname)
Employee.add_increment(3)
harry.increase()
print(harry.salary)