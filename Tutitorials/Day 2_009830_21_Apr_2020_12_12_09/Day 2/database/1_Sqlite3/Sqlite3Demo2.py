import sqlite3 
conn = sqlite3.connect('test')
cursor = conn.cursor()
print ("cursor = ",cursor)
cursor.execute('''DROP TABLE studentdata2''')
conn.commit()

cursor = conn.cursor()
cursor.execute("create table studentdata2(name text, count integer)")
conn.commit()


cursor = conn.cursor()
cursor.execute("insert into studentdata2 (name, count) values (?, ?)",("Jill", 15))
result = cursor.execute("select * from studentdata2")
print(result.fetchall())
"""
print ("-----------------------------------")
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns name count
    print('{0} :{1}'.format(row[0], row[1]))
print ("-----------------------------------")
"""
conn.commit()
conn.close()

"""
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} :{1}'.format(row[0], row[1]))

"""
