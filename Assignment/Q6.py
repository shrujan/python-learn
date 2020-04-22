class Employee:
    count = 0
    
    def __init__(self, name, salary):
        Employee.count += 1
        self.name = name
        self.salary = salary
        print(Employee.count)

    def displayEmployee(self):
        print('Hello %s Enjoy your salary of %s' % (self.name, self.salary))


e1 = Employee('Shrujan', '60000')
e1.displayEmployee()