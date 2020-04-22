

#Assignment 7
#!/usr/bin/python
#A Python program to sort a list of names by length of the names, from shortest to longest
print('*******[ Welcome to List sorter ]*******')

list1 = [999,10,20,30]
list1.sort() #modifies original list
print ("Sorted list = ", list1)#[10, 20, 30, 999]


print ("Sixe of list1 = ", len(list1))
unsortedList = ['zzz','bb','Aaaa', 'cccccccc', 'zzzzzzzzzzzz']		
sortedList = (sorted(unsortedList))
print ('Unsorted list is ', unsortedList)
print ("Default sorted list = ", sortedList)

sortedListbylen = sorted(unsortedList,key=len)# len(unsortedList[0]),len(unsortedList[1])
print ("sorted list by len = ", sortedListbylen)


"""
sorted(
len(unsortedList[0]) -4
len(unsortedList[1]) -2
)
"""
#map(fun, list1) #fun(list1[0], 
#print 'Sorted list is ', sortedList

#len("abc")
#sorted(

"""
dessortedList = sorted(unsortedList, key=len, reverse=True)# len(unsortedList[0])
print 'Sorted list is ', dessortedList
"""
"""functional programming """

#len(list1)




