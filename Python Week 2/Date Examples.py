from datetime import datetime, timedelta
from time import sleep

#https://www.programiz.com/python-programming/datetime/strftime
#%Y, %m, %d etc. are format codes. 
# The strftime() method takes one or more format codes as an argument and 
# returns a formatted string based on it.

now = datetime.now() # current date and time
print("the date is" + str(now))

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	

# calculate the delta
current_date = datetime.now()
#sleep(62)
current_date2 = datetime.now()

delta_sec = current_date2 - current_date
print("delta is " + str(delta_sec.seconds) + " seconds")

# print yesterday's date
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))

# ask a user to enter a date
date_entered = input('Please enter a date (mm/dd/yyyy): ')
date_entered = datetime.strptime(date_entered, '%m/%d/%Y')

date_entered2 = input('Please enter a date (mm/dd/yyyy): ')
date_entered2 = datetime.strptime(date_entered2, '%m/%d/%Y')

delta = date_entered - date_entered2
print(delta.days)
years = date_entered2.year - date_entered.year
months = date_entered2.month - date_entered.month

if months < 0:
    years = years -1
    months = months + 12
print(f"You are {years} years and {months} months younger")


# print the date one week from the date entered
#Once we have a date object, we can take advantage of powerful methods for working witht time.
one_week = timedelta(weeks=1,days=1)
one_week_later = date_entered + one_week
print('One week later it will be: ' + str(one_week_later))