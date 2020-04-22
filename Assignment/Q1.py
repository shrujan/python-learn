

unsortedList = ['Aaaa', 'bb' , 'cccccccc', 'ooo','zzzzzzzzzzzz']
unsortedListLength = len(unsortedList)
count = 0

print(unsortedListLength)

for i in range(unsortedListLength):

    for j in range(0, unsortedListLength-1):
        l1 = len(unsortedList[j])
        l2 = len(unsortedList[j + 1])
        print ('l1 = ', l1, 'l2 = ', l2) 
        if (l1 > l2):
            temp =  unsortedList[j]
            unsortedList[j] = unsortedList[j + 1]
            unsortedList[j + 1] = temp

print(unsortedList) # now ordered
