

import sqlite3 
conn = sqlite3.connect('test')  #local file name 'test'
cursor = conn.cursor()  #channel as cursor object between ur python script and the backened database file-test
print ("cursor = ",cursor)
#cursor.execute("create table studentdata444(name text, count integer)")
cursor.execute("insert into studentdata444(name, count) values(?,?)",("Jill",15))
cursor.execute("insert into studentdata444 (name, count) values (?, ?)",("NIL", 25))
result = cursor.execute("select * from studentdata444")
print ("Result = ", result)
print(result.fetchall())
#[('Jill', 15), ('NIL', 25)]
conn.commit()
conn.close()
