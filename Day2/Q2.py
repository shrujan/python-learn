List1 = [47,11,42,102,13]


def findMax(list):
    maximum = 0
    for l1 in list:
        if l1 > maximum:
            maximum = l1

    return maximum

maximum = findMax(List1)

print('Max value = ', maximum )

# # OR 

# print("Max == ",max(List1))


