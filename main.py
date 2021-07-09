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

dicto = {
    'e1': ['shlok', 'koirala', 90000],
}

for i in dicto:
    print (dicto[i][0])
    shlok = Employee(dicto[i][0], dicto[i][1], dicto[i][2])

print (shlok.fname, shlok.lname, shlok.salary)