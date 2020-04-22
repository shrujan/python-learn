


from operator import itemgetter   #operator is  module file
#sort data by age

student_tuples = [ ('john', 'A', 25), ('janele', 'B', 32), ('ni', 'B', 50),('dav', 'B', 28) ] #list of tuples

#sorted , lambda
sorted_students_byAge = sorted(student_tuples, key=lambda s: s[2])
sorted_students_byAge_rev = sorted(student_tuples, key=lambda s: s[2], reverse=True)
# sort by age
#(lambda s: s[2])(student_tuples[0])
#                               ('john', 'A', 25)

#2. #(lambda student: student[2])(student_tuples[1])
print ("Student data = ", student_tuples)   #Student data =  [('john', 'A', 25), ('jane', 'B', 32), ('nil', 'B', 50), ('dave', 'B', 28)]
print ("Sorted students by age = ",sorted_students_byAge) #Sorted students by age =  [('john', 'A', 25), ('dave', 'B', 28), ('jane', 'B', 32), ('nil', 'B', 50)]
print ("Sorted students by age in desceding = ",sorted_students_byAge_rev) #
print ("-------------------------------------------------------------------")

sorted_students_byAge1 =  sorted(student_tuples, key=itemgetter(2))
print ("Student data = ", student_tuples)  #Student data =  [('john', 'A', 25), ('jane', 'B', 32), ('nil', 'B', 50), ('dave', 'B', 28)]
print ("Sorted students by age = ",sorted_students_byAge1)  #Sorted students by age =  [('john', 'A', 25), ('dave', 'B', 28), ('jane', 'B', 32), ('nil', 'B', 50)]
print ("-------------------------------------------------------------------")

#multiple levels of sorting
sorted_students_byAge_Grade = sorted(student_tuples, key=itemgetter(1,2))
print ("Sorted students by grade and age = ",sorted_students_byAge_Grade) #Sorted students by grade and age =  [('john', 'A', 25), ('dave', 'B', 28), ('jane', 'B', 32), ('nil', 'B', 50)]
print ("-------------------------------------------------------------------")
sorted_students_byNamelen = sorted(student_tuples, key=lambda student: len(student[0])) # sort by age
print ("Sorted students by Name len = ",sorted_students_byNamelen) #Sorted students by age =  [('john', 'A', 25), ('dave', 'B', 28), ('jane', 'B', 32), ('nil', 'B', 50)]















print ("-------------------------------------------------------------------")



"""
import math
math.sqrt(25)

from math import *
sqrt(25)
"""




























