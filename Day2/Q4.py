import sqlite3

conn = sqlite3.connect('users')
cursor = conn.cursor()

cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user_details' ''')


if cursor.fetchone()[0]==1:
    print('Table exists.. Deleting now. ')
    res = cursor.execute("drop table user_details")

print('************ creating a new table ***************')
cursor.execute('create table user_details ( name, phone, email, password)')

userChoice = 'y'

while userChoice == 'y':

    name = input('Enter name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')
    password = input('Enter password: ')

    cursor.execute('insert into user_details values(?,?,?,?)', (name, phone, email, password))
    conn.commit()

    print('************* New User Created **********')

    res = cursor.execute("select * from user_details where name = '" + name +"'")
    user = res.fetchone()
    print(' Name = ', user[0], ' \n Phone = ', user[1], '\n Email = ', user[2], ' \n Password = ', user[3])

    userChoice = input('Enter new User (y/n) ?  ')

print('************* Fetch User **********')
userName = input('Enter User Name to fetch the Details... ')
res = cursor.execute("select * from user_details where name = '" + userName +"'")
user = res.fetchone()

print('************* User Details **********')
if user == None:
    print(' User Does not exist ... ')
else:
    print(' Name = ', user[0], ' \n Phone = ', user[1], '\n Email = ', user[2], ' \n Password = ', user[3])










