
empDictonary = {'6a':30000,'2a':40000}
sortedEmpDictonary = {}


total = int(input ('Enter total number of elements '))

for i in range(total):
    str1 = input("Enter emp ID:salary in a single line: ")
    l1 = str1.split(":")
    empDictonary[l1[0]] = l1[1]

# sort empDictonary
empKey = list(empDictonary.keys())
empKey.sort()                   

print('---------------------------------')

for key in empKey:
    print('Id == ',key, "Salary == ",  empDictonary[key])
    sortedEmpDictonary[key] = int(empDictonary[key]) + 5000

print(sortedEmpDictonary)




