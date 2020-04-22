        #map function
#import math          #math.sqrt(5)
from math import *    #sqrt(5)
r = [0, 1, 2, 3, 4, 5, 6]
map_obj = map(cos, r)               #Math.cos(4)       #-------3)
print ("Map Object =",map_obj)      #<map object at 0x0410A9B0>
target_list = list(map_obj)
print ("Target  list =",target_list)      #Target  list = [1.0, 0.5403023058681398, -0.4161468365471424, -0.9899924966004454, -0.6536436208636119, 0.28366218546322625, 0.960170286650366]
print ("---------------------------------------------")

squares = [4,9,16,25,36]
squareroot_list = list(map(sqrt, squares ))   #Target squareroot list = [2.0, 3.0, 4.0, 5.0, 6.0]
print("Original squares list = ",squares)           #[4, 9, 16, 25, 36]
print ("Target squareroot list =",squareroot_list)  #[2.0, 3.0, 4.0, 5.0, 6.0]



int_list = list(map(int, squareroot_list ))
print ("Target int list =",int_list)      #Target int list = [2, 3, 4, 5, 6]
print ("---------------------------------------------")


words =["abc", "xyz", "lmn"]
upper_words = []
upper_words = list(map(lambda w :w.upper() , words))
#in Python3 map() function returns map object so pass that as parameter to list

print ("Original words = ", words)    #['abc', 'xyz', 'lmn']
print ("Upper words = ",upper_words)  #['ABC', 'XYZ', 'LMN']




"""
map(
(lambda w :w.upper())(words[0]i.e abc) --->ABC
(lambda w :w.upper())(words[1]i.e xyz) --->XYZ
(lambda w :w.upper())(words[2]i.e lmn) --->LMN
) ------> ["ABC", "XYZ", "LMN"]
"""


"""
words= ["abc", "pqr", "xyz"]

a=lambda str1 : str1.upper()

mObj=map(a, words)            # ['ABC', 'PQR', 'XYZ']
print "mObj = ", mObj






"""



"""
s1 = "abc"
upper_s1 = s1.upper()
print "Original string = ", s1
print "Upper string  = ", upper_s1
"""








"""
for i in listOne:                               #1)
    new_listOne.append(i*2)


#OR
new_listOne1 =[x*2 for x in listOne if (x<0)]   #list comprehension    #2)
print "Updated new list = ", new_listOne1



Built-in function that works on a list
'map' takes a function and a list  (2 arguments)
   The function must take only one argument, and return one value
   The function is applied to each value of the list
   The resulting values are returned in a list

map reduce filter

for i in f:
    target_list.append(sqrt(i))
"""







