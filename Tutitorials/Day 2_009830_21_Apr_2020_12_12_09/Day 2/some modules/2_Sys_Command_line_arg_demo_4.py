
#command line argumnets
#2_Sys_Command_line_arg_demo_4.py
import sys
#print ("Command line arguments = ", sys.argv)  #it is  a list of strings




print ("--------------------------------------------")
if (len(sys.argv)==3):
    print ("Command line arguments = ", sys.argv)
    print ("File name = ", sys.argv[0])
    print ("argv[1] = ", sys.argv[1])
    print ("argv[2] = ", sys.argv[2])
else:
    print ("Insufficient args!!!!!")


















"""
if (len(sys.argv)==2):
    print "argv list = ",sys.argv   #is a list
    print "First argumnet fron argv list = ",sys.argv[0]  #current file name
    print "Second argument from argv list =",sys.argv[1]
    print dir(sys)
else:
    print "Insufficient arguments!!!try again!!!"



# sys.argv is a list   ['file name', , ]
"""
