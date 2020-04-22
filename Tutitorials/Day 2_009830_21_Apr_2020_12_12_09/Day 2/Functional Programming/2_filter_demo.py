
#2_filter_demo.py
    #filter
r = [0, 1, 2, 3, 4, 5, 6]
def large(x):
    return x>3                #user defined function, will return True if cond is satisfied
    #return "Hello"


filter_obj = filter(large, r)  #large(0), large(1),   large(2), large(3),large(4)
target_list = list(filter_obj)
print ("Original list = ",r)
print("filter_obj = ", filter_obj)        #<filter object at 0x046AAB10>
print ("Target list = ",target_list)      #Target list =  [4, 5, 6]
print ("---------------------------------------------------------")

def lowercase(x): return x.islower()

words =['abc', 'XYZ','lmn','NIL']
lower_words =list(filter(lowercase,words))#lowercase(words[0])
print ("Words = ",words)                      #Words =  ['abc', 'XYZ', 'lmn', 'NIL']
print ("Lower Case words = ",lower_words)     #

upper_words =list(filter(lambda x :x.isupper(),words))
print ("Upper Case words = ",upper_words)     #Upper Case words =  ['XYZ', 'NIL']

print(((lambda x :x.isupper())("ABC")) #True

'''
Built-in function that works on a list
'filter' takes a function and a list
It uses the function to decide which values to put into the resulting list
    Each value in the list is given to the function
    If the function return True, then the value is put into the resulting list
    If the function returns False, then the value is skipped
'''
'''
map
reduce
filter

'''
