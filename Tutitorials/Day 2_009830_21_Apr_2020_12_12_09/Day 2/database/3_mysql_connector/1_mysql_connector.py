
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

"""
MySQL Connector Python has the following advantages: –
MySQL Connector Python is written in pure Python, and it is self-sufficient to execute database queries through python.
It is an official Oracle-supported driver to work with MySQL and python.
It is Python 3 compatible, actively maintained.

This Python MySQL session mainly focuses on: –
How to install MySQL Connector Python and use its functions to access the MySQL database.
Perform MySQL CRUD operations such as data insertion, data retrieval, data update, and data deletion using Python.

mysql-connector-python module Installation:
Using pip command :
Open Anaconda Command prompt as administrator :
Go to start menu ->Anaconda 3->Anaconda prompt
Use cd\ to come out of set directory or path.
Run pip install command as:
>pip install mysql-connector-python


Understand the Python MySQL Database connection program:-

import mysql.connector
This line imports the MySQL Connector Python module in your program so you can use this module’s API to connect MySQL.
from mysql.connector import Error
mysql connector Error object is used to show us an error when we failed to connect Databases or if any other database error occurred while working with the database. Example ACCESS DENIED ERROR when username or password is wrong.

mysql.connector.connect()
Using this method we can connect the MySQL Database, this method accepts four required parameters: Host, Database, User and Password that we already discussed.
connect() method established a connection to the  MySQL database from Python application and returned a MySQLConnection object.  Then we can use MySQLConnection object to perform various operations on the MySQL Database.
The Connect()  method can throw an exception, i.e. Database error if one of the required parameters is wrong. For example, if you provide a database name that is not present in MySQL, then Python application throws 
an exception. So check the arguments that you are passing to this method.

connection.is_connected() 
is_connected() is the method of the MySQLConnection class through which we can verify is our python application connected to MySQL.

 connection.cursor()
This method returns a cursor object. Using a cursor object, we can execute SQL queries.
The MySQLCursor class instantiates objects that can execute operations such as SQL statements.
Cursor objects interact with the MySQL server using a MySQLConnection object.

cursor.close()
Using the cursor’s close method we can close the cursor object. Once we close the cursor object, we can not execute any SQL statement.
 connection.close()
At last, we are closing the MySQL database connection using a close() method of MySQLConnection class.



"""
