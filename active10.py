# import datetime 
# now = datetime.datetime.now()
# next_year = datetime.datetime(2027,1,1)
# remaining_days = next_year - now 
# print("current date and time :",now.strftime("%Y-%m-%d %H:%M:%S"))
# print("days left until the new year:",remaining_days.days)

# import datetime 
# now = datetime.datetime.now().replace(microsecond=0)
# next_year = datetime.datetime(2027,1,1)
# remaining_days = next_year - now 
# print("current date and time :",now)
# print("days left until the new year:",remaining_days.days)

import datetime 
now = datetime.datetime.now().replace(microsecond=0)
next_year = datetime.datetime(2027,1,1)
remaining = next_year - now 
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) //60
second = (remaining.seconds % 3600 ) % 60 
print("current date and time :",now)
print(f"days left until the new year: {days} days ,{hours} hours , {minutes} minutes , {second}second")