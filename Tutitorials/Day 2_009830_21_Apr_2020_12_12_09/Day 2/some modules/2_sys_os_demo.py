
#2_sys_os_demo.py
import sys
import os

if(os.path.exists("myfile111.txt")):
        sys.stderr.write("File already exists")
        sys.exit(1)
f=open("myfile.txt","w")
f.write("Hello World\n")
f.close()
f =open("myfile.txt","r")
while True:
        x = f.readline()
        if x: print (x)
        else: break
print ("------------------------------------------------------")
print (os.listdir('.'))
os.chdir('C:\\ASL_June')    #provide dir path
os.mkdir("temp")  #provide dir path
os.chdir('C:\\ASL_June')
f1=open("myfile99.txt","w")
f1.close()
print  ("---------------------------------------------")








