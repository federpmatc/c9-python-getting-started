from datetime import datetime, timedelta
#https://www.programiz.com/python-programming/datetime/strftime
#%Y, %m, %d etc. are format codes. 
# The strftime() method takes one or more format codes as an argument and 
# returns a formatted string based on it.

date_entered = input('Please enter a date1 (dd/mm/yyyy): ')
date_entered = datetime.strptime(date_entered, '%d/%m/%Y')

date_entered2 = input('Please enter a date2 (dd/mm/yyyy): ')
date_entered2 = datetime.strptime(date_entered2, '%d/%m/%Y')

delta=date_entered2 -date_entered
print(delta)
print(delta.days)
print(delta.total_seconds())
