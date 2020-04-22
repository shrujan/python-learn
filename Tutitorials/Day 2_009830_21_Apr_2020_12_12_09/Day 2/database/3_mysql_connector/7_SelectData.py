import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
    sql_select_Query = "select * from Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)
    print ("All fetched records = ",records)#list of tuple records

    print("\nPrinting each laptop record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
    

"""
Note:  To fetch data use cursor.execute() to run a query.
cursor.fetchall() to fetch all rows .
cursor.fetchone() to fetch single row.
cursor.fetchmany(SIZE) to fetch limited rows.
"""
