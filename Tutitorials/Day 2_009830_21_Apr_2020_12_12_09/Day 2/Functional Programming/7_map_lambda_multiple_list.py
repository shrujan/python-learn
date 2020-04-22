

#7_map_lambda_multiple_list.py
a = [1,2,3,4]  #all list with same number of list
b = [17,12,13,14]
c = [-1,-4,5,9]
def additionFun(x,y):
    return x+y

additionlist = list(map(additionFun, a,b))  #additionFun(a[0],b[0])
print ("Original list a = ",a)
print ("Original list b = ",b)
print ("Addition list = ",additionlist)
print ("---------------------------------------------")
print ((lambda x,y:x+y)(10,20))
print ("---------------------------------------------")

m1 = map(lambda x,y:x+y, a,b)
print (list(m1))
                                #[18, 14, 14, 14]

print (list(map(lambda x,y,z:x+y+z, a,b,c)))
                                #[17, 10, 19, 23]

print (list(map(lambda x,y,z:x+y-z, a,b,c)))
                                #[19, 18, 9, 5]









