


#2_sys_err_demo_2.py
import sys
sys.stderr = open("error1.txt", "a")

print ("nosuchvar = ",nosuchvar)   #Namerror gets printed in file error.txt

sys.stderr.close()
























"""
temp = sys.stderr

sys.stderr = temp  #o/p will come back to consle err
print nosuchvar


"""
