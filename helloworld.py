msg = "welcome to the matrix"
print('hello, shrujan', msg)

x = 5
print(x)

x = "hello" + '\n welcome'
print(x)

# append string
x += ' max payne'

print(x)

# floor division res will be in int = 6
floorDivision = 20//3

# result will be in float  = 6.0 
floorDivision = 20//3.0


print (floorDivision, 20/3)

#  precidence 
# ()
# **  - exponential
# %, / , //, *
# +, -

sum = (16.68 + 6.98 +  16.78 + 15.26 + 3.00 + 4.39)
print(round(sum , 2))


stri = "voila!"
print(stri[:3]) # char from index 0 to 3
print(stri[1:4]) # char from index 1 to 4
print(stri[2]) # char at second index 

# type is similar to typeof in JS
boolType = True
strType = 'shr'
intType = 12
floatType = 12.00


print(type(boolType))
print(type(strType))
print(type(intType))
print(type(floatType))

# str() converts to string 
print('==========')

boolType = str(True)
strType = str('shr')
intType = str(12)
floatType = str(12.00)

print(type(boolType))
print(type(strType))
print(type(intType))
print(type(floatType))

# -------------------------
print("****** \n ****  \n  **  \n  *")

# input and output

name = input('Enter you name: ')
print('your name is ' + name + '.') # this is always string

age = input("Enter age ")
print('your age is '+ age)

# print('your age is '+ int(age)) #error cannot concatinate string with int



# ---------------------
# FUNCTION
print('----------------')
mainStr = 'Hello '


# Default return of a function is NoneType
def funName (param1, param2, param3 = 'orange'):
    print('sampleFN')
    print(param1 + ' shrujan aged ' + str(param2) + '. Your fav fruit is ' + param3 )
    return "THanks"

funName(mainStr, 23, 'apple')
ret = funName(mainStr, 30)
print(ret)

