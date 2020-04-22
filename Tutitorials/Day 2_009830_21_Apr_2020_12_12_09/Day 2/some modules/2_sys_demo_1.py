

"""sys. stdin  stdout stderr"""

import sys
sys.stdout = open("hello.txt","w")
print ("AAAAAAAAAAAAAAAAaa")  #instead of printing on console, it will print inside file hello.txt 
sys.stdout.close()


























'''
stdin
stdout
stderr
#!/usr/bin/env python

 f1 = open("hello.txt","w")
 f1.write("Hello !!!")
'''
