from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print ("d = ",d)
print ("Handling", d.popleft())
print (dir(d))

'''
The collections module provides a deque() object that is like a list with
faster appends and pops from the left side but slower lookups in the middle.
'''
