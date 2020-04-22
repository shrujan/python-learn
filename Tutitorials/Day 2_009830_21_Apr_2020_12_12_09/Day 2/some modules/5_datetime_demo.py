

#5_datetime_demo.py

from datetime import date     #date is a class
now = date.today()
print ("Today is = ",now)    #Today is =  2019-12-24

Ord1 = now.toordinal()+3   #dyas incremented by 3     
print (date.fromordinal(Ord1).strftime('%m-%d-%y'))     #07-20-19

print ("-------------------------------------------------------------")
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print (age.days)

print ("-------------------------------------------------------------")
print (dir(date))
