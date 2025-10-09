#Iterators and Generators
#An iterator is an object that can be iterated (looped) over.
'''
It implements two methods:
__iter__() → returns the iterator object itself.
__next__() → returns the next value each time it’s called.
'''
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

'''
A generator is a special kind of iterator that is created using the yield keyword instead of return.
It does not store all values in memory, it yields one value at a time, which saves memory.
'''
def my_gen():
    for i in range(3):
        yield i

for num in my_gen():
    print(num)
 #---------------------------------------------------------------------------------------------------------
 #Dates and Time
'''
o  Get the current date and time.
o  Do date arithmetic (add or subtract days).
o  Remove unnecessary precision like microseconds.
o  Find differences between two dates in seconds, minutes, etc.
'''
from datetime import datetime, date, timedelta
'''
datetime → gives both date and time.
date → gives only the date (year, month, day).
timedelta → represents the difference between two dates/times (e.g. 5 days, 10 hours, etc.).
'''
from datetime import datetime

now = datetime.now()

print("Weekday short:", now.strftime("%a"))
print("Weekday full:", now.strftime("%A"))
print("Day of month:", now.strftime("%d"))
print("Month short:", now.strftime("%b"))
print("Month full:", now.strftime("%B"))
print("Year full:", now.strftime("%Y"))
print("Local datetime:", now.strftime("%c"))
print("24-hour time:", now.strftime("%H:%M:%S"))
print("12-hour time:", now.strftime("%I:%M:%S %p"))
print("Day of year:", now.strftime("%j"))
print("Week number:", now.strftime("%U"))
print("Literal percent:", now.strftime("%%"))
