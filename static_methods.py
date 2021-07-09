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

    @staticmethod
    def isopen(day):
        if day == "Sunday" or day == "sunday":
            return False
        else:
            return True


print(Employee.isopen("Monday"))
