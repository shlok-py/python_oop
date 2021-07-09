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


Employees = [Employee('shlok', 'koirala', 8000), Employee(
    'adam', 'niraula', 10000), Employee('kiran', 'Das', 8600)]

for i in range(len(Employees)):
    print(Employees[i].fname)
