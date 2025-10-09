#Subtract five days from the current date

from datetime import date, timedelta
current_date = date.today()
new_date = current_date - timedelta(days=5)
print("Current date:", current_date)
print("Date five days ago:", new_date)

#-------------------------------------------------------------------------------------
#Print yesterday, today, and tomorrow

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#-------------------------------------------------------------------------------------------
#Drop microseconds from a datetime

from datetime import datetime
now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:", no_microseconds)
#-----------------------------------------------------------------------------------------------
#Calculate difference between two dates in seconds

from datetime import datetime
date1 = datetime(2025, 10, 8, 14, 30, 0)
date2 = datetime(2025, 10, 8, 15, 45, 30)
difference = date2 - date1
seconds = difference.total_seconds()
print("Difference in seconds:", seconds)
