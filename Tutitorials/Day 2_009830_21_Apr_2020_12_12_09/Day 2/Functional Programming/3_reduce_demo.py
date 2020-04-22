    #reduce works in Python 2 but NOT in Python3

r = [0, 1, 2, 3, 4, 5, 6]
def sum(x, y): return x+y
ans = sum(10,20)
print ("addition of 10 and 20 =", ans)   #addition of 10 and 20 = 30
print ("-------------------------------------------------")
print (reduce(sum, r))        #21   sum(0,1)   sum(1,2) =3    sum(3,3)

def plus(x,y):

    return(x+y)


lst=['h','e','l','l','o']

print("return of reduce = ",reduce(plus,lst))  #hello


'''
Built-in function that works on a list (sequence)
'reduce' takes a function and a list
It boils down the list into one value using the function
    The function must take only two arguments, and return one value
    'reduce' applies the function to the first two values in the list
    The function is then applied to the result and the next value in the list
    And so on, until all values in the list have been used

'''

