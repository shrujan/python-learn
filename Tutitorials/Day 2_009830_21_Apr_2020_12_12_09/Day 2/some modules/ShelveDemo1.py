

import shelve
'''Following code creates a database and stores dictionary entries in it.'''
s = shelve.open("test")
s['name'] = "Ajay"
s['age'] = 23
s['marks'] = 75
s.close()

'''To access value of a particular key in shelf.'''

s=shelve.open('test')
print ("Age = ",s['age'])

#The items(), keys() and values() methods return view objects.
print("list(s.items())  = ",list(s.items()) ) #[('name', 'Ajay'), ('age', 23), ('marks', 75)]
print("list(s.keys())  =",list(s.keys()) )    #['name', 'age', 'marks']
print("list(s.values()) = ",list(s.values())) #['Ajay', 23, 75]

#To remove a key-value pair from shelf
s.pop('marks')
print("list(s.items())  = ",list(s.items()) ) #[('name', 'Ajay'), ('age', 23)]
