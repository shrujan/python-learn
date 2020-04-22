
#PickleDemo.py   shelve
#Data persistence/ permanent storage of Python ojects
#serialization / deserialization
import pickle

a = 100                 #int
b = "PSL"               #str
c = [3.1456,'x','y']    #list

file = open("state.txt", 'ab')
#file.write("abc")
pickle.dump(a, file)    #saves the Python objects in some pickle string foramt
pickle.dump(b, file)
pickle.dump(c, file)
file.close()
print ("----------------------------------------------------")

file = open("state.txt", 'rb')
#file.read()  instaed of this methos, go for load () method
a1 = pickle.load(file)   #load() function reads the object back  int
b1 = pickle.load(file)  #str
c1 = pickle.load(file)  #list
print ("a1= ",a1, "type of a1 = ", type(a1))#a1=  100 type of a1 =  <class 'int'>
print ("b1= ",b1, "type of b1 = ", type(b1))#b1=  PSL type of b1 =  <class 'str'>
print ("c1= ",c1, "type of c1 = ", type(c1))#c1=  [3.1456, 'x', 'y'] type of c1 =  <class 'list'>
file.close()

#shelve  module








