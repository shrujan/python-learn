
#filter and lambda examples
print ("-------------------------------------------------------")
r = [0, 1, 2, 3, 4, 5, 6]
target_list = list(filter(lambda x:x>3, r))
print ("target list = ",target_list )          #target list = [4, 5, 6]

words =["abc","PSL", "XYZ","aaa","bbb"]
upperwords = list(filter(lambda str:str.isupper(),words))
print ("Upperwords = ",upperwords  )          #Upperwords =  ['PSL', 'XYZ']
























"""
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result
                #[1, 1, 3, 5, 13, 21, 55]


"""
