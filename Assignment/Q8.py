
empFiles = open('TextFiles/empData.txt', "r")
employeeDictonary = {}

while True:
        line = empFiles.readline()
        if line:
                Line = line.rstrip()
                emp = Line.split(":")
                employeeDictonary[emp[0]] = emp[1:]
        else:
                print ("Nothing in file")
                break

        
empFiles.close()

keys = list(employeeDictonary.keys())
keys.sort()

for k in keys:
    print("Id = ", k, " Name = ", employeeDictonary[k][0], " Age = ", employeeDictonary[k][1], " Age = ", employeeDictonary[k][2])
