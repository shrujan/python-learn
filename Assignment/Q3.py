
total = int(input ('Enter total number of elements '))
numList = []

for i in range(total):
    numList.append(int(input('Enter '+  str(i+1) +' number.')))

numList.sort()

print(numList)

