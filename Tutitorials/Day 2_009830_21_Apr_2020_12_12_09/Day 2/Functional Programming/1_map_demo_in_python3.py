

#in python 3
words =["abc", "xyz", "lmn"]
upper_words = []
map_ob = map(lambda w :w.upper() , words)
print( "Return value of map in Python 3 = ", map_ob)
upper_words = list(map_ob)
print ("Original sequence list = ", words)
print("Upper words = ", upper_words)


#in Python3 map() function returns map object so pass that as parameter to list
