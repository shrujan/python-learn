import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
    sql_Query = "select price from laptop where id =%s"
    id = (2,)
    cursor = connection.cursor()
    cursor.execute(sql_Query, id)
    record = cursor.fetchone()
    print("One record = ", record)          #One record =  (6999.0,)
    # selecting column value into varible
    price = float(record[0])
    print("Laptop price is : ", price)      #6999.0

except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    
