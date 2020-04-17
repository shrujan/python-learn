import random

print(random.randint(1, 10))

# OR

# from random import randint

# print (randint(12, 20))

# OR 

from random import * # import all function from random

print(random())


# comparison

print(1  > 2)
print (1 != 2)
print ('Hi' == 'hi')  # false because of case sensitive

a = 1
b = 2

print ( (a == 1) and (b == 2))
print ( (a == 1) or (b == 3))

#  if else

choice = input('want to enter validate marks ')




if choice == 'yes':
    print('hello')
    mar = input('want to enter validate marks ')

    if int(mar) > 20:
        print('pass')
    else:
        print('fail')
elif choice == 'maybe':
    print('Make up your mind already')
else:
    print('else')
