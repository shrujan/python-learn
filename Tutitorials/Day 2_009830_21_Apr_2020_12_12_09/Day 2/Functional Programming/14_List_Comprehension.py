#List Comprehension
listOne=[1,2,3]
new_listOne =[x*2 for x in listOne ]
#comprehenstion to operate on every element
print ("list one =", listOne)     #[1,2,3]
print ("new list =", new_listOne) #[2,4,6]


str ="abc"
print (str.upper())

words =["abc","xyz", "lmn","aaaa","bbb"]
upperwords =[i.upper() for i in words]
print ("Original words = ",words)
print ("Upper words =",upperwords)

print ("-------------------------------------------------")
square_list = [x**2 for x in listOne]
print ("Square list =",square_list)
print ("-------------------------------------------------")

#dictionary comprehension
dictionaryOne = [1, 2, 3, 4]   #it is  a list
dictionaryTwo = {x: x * x for x in dictionaryOne }     #{1:1, 2:4, 3:9, 4:16}
print (dictionaryTwo)
print ("-------------------------------------------------")


#d={'a':56000}














































#d1 ={'a1':100,'b1':200}











"""
a=[1,2,3,4,5]
revB = [reverse a]
print "Rev B= ", revB

for i in listOne:
    listTwo.append(i**2)

"""
