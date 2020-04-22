#Python MySQL call Stored Procedure
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
    cursor = connection.cursor()
    cursor.callproc('get_laptop', [2, ])
    # print results
    print("Printing laptop details")
    for result in cursor.stored_results():
        print(result.fetchall())

except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")





"""
Open MySQL console and run the below query to create a MySQL Stored Procedure.
DELIMITER $$
USE Electronics$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_laptop`(IN d_id int)
BEGIN
select * from Laptop where id = d_id;
END $$
DELIMITER ;
"""
