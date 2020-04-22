import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
    mySql_select_Query = "select * from laptop"
    cursor = connection.cursor(buffered=True)
    cursor.execute(mySql_select_Query)
    fetching_size = 2
    records = cursor.fetchmany(fetching_size)

    print("Total number of rows is: ", cursor.rowcount)
    print("Printing ", fetching_size, " Laptop record using cursor.fetchmany")
    for row in records:
        print(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("connection is closed")
