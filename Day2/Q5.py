import sqlite3

conn = sqlite3.connect('emp_details.db')
cursor = conn.cursor()

#get the count of tables with the name
cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='employees' ''')

#if the count is 1, then table exists
if cursor.fetchone()[0]==1:
    print('Table exists. Deleting old table ... ')
    cursor.execute("drop table employees")


print('************ creating a new table ***************')
cursor.execute('create table employees ( empId, name, age, salary)')

print( '************ INSERT 5 Employees ***********************' )
# insert 5 employees
cursor.execute('insert into employees values (? , ? , ? , ?) ', ('001', 'Raju', 23, 30000))
cursor.execute('insert into employees values (? , ? , ? , ?) ', ('002', 'Suresh', 40, 40000))
cursor.execute('insert into employees values (? , ? , ? , ?) ', ('003', 'Gopal', 30, 43000))
cursor.execute('insert into employees values (? , ? , ? , ?) ', ('004', 'Hari', 24, 23000))
cursor.execute('insert into employees values (? , ? , ? , ?) ', ('005', 'Vickey', 34, 50000))
conn.commit()
print(' ****************** insertion Done ***********************************')

class Employees:
    def __init__(self, id, name, age, salary):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary

    def showEmployees(self):
        print(" ---------------------------- ")
        print('Id:- ', self.id)
        print('Name:- ', self.name)
        print('Age:- ', self.age)
        print('Salary:- ', self.salary)


# read employee from DB 
res = cursor.execute('select * from employees')
employeeList = res.fetchall()

for emp in employeeList:
    empObj = Employees(emp[0], emp[1], emp[2], emp[3])
    empObj.showEmployees()


