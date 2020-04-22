

#2_sys_stdout_demo_3.py
import sys
temp = sys.stdout

f = open("hello.txt", "w")
sys.stdout = f
print ("This is fun")

sys.stdout = temp  #restored the default implemenation of sys.stdout to the screen
f.close()
print ("This is even more fun")

print (sys.version)

print (str(sys.version).split('.')[0:2])

print (str(sys.version).split('.')[0])    #this can be used to check version 2 or 3

if int(str(sys.version).split('.')[0])==2:
        print ("Version 2")
else:
        print ("Not Supported")

print ("==================================================================================")
print (dir(sys))
print ("====================================================================================")















#print os.open().__doc__
