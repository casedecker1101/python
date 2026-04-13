# 17.1 creating a date
import datetime
ada_bday = datetime.date(1815, 12, 10)
print(ada_bday)

# 17.2 prompting for a date
year = input("Please enter a year from 1900 to 2100: ")
while True:
    if int(year) >= 1900 and int(year) <= 2100:
        break
    else:
        year = input("Please enter a VALID year from 1900 to 2100: ")

month = input("Please enter a month from 1 to 12: ")
while True:
    if int(month) >= 1 and int(month) <= 12:
        break
    else:
        month = input("Please enter a VALID month from 1 to 12: ")

day = input("Please enter a day from 1 to 31: ")
while True:
    if int(day) >= 1 and int(day) <= 31:
        break
    else:
        day = input("Please enter a VALID day from 1 to 31: ")

user_date = datetime.date(int(year), int(month), int(day))
print(user_date)

# 17.3 creating a time
appointment = datetime.time(10, 30, 00)
print("Appointment time: " + str(appointment))

# 17.4 creating a datetime
appointment = datetime.datetime(2022, 12, 10, 10, 30, 00)
print("Appointment time: " + str(appointment))

# 17.5 what time is it
time_now = datetime.datetime.now()
print(time_now)

# 17.6 splitting a date
d = "2022-07-23 11:26:26.047342"
(d,t) = d.split()
(year, month, day) = d.split("-")
print(year)
print(month)
print(day)

# 17.7 splitting the time
d = "2022-07-23 11:26:26.047342"
(d,t) = d.split()
(hour, minute, second) = t.split(":")
print(hour)
print(minute)
print(second)

# 17.8 splitting the date and time
d = datetime.datetime.now()
d = str(d)

(d,t) = d.split()
(year, month, day) = d.split("-")
(hour, minute, second) = t.split(":")

print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)

# 17.9 extracting with datetime attributes
time_now = datetime.datetime.now()
print(time_now)

print(time_now.year)
print(time_now.month)
print(time_now.day)
print(time_now.hour)
print(time_now.minute)
print(time_now.second)
print(time_now.microsecond)
print(time_now.tzinfo)

# 17.10 creating a custom date with named parameters
t1 = datetime.date(year = 2013, day = 4, month = 12)
t2 = datetime.date(year = 2013, month = 12, day = 4)
t3 = datetime.date(day = 4, year = 2013, month = 12)
t4 = datetime.date(day = 4, month = 12, year = 2013)
t5 = datetime.date(month = 12, year = 2013, day = 4)
t6 = datetime.date(month = 12, day = 4, year = 2013)

print(t1,t2,t3,t4,t5,t6)

# 17.11 omparing dates
d1 = datetime.datetime(year = 2013, month = 12, day = 4)
d2 = datetime.datetime(year = 2014, month = 3, day = 12)

print(d1 > d2) # check if d1 is more recent than d2
print(d1 < d2)
print(d1 == d2)

# 17.12 past, future or present
year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: "))

d1 = datetime.date(year,month,day)
today = datetime.datetime.today().date()

if d1 > today:
    print("That date is in the future.")
elif d1 < today:
    print("That date is in the past.")
elif d1 == today:
    print("That date is today!")

# 17.13 Working with UTC dates 
time_utc_now = datetime.datetime.utcnow()
print(time_utc_now)
print("-" * 30)
print(time_utc_now.year)
print(time_utc_now.month)
print(time_utc_now.day)
print(time_utc_now.hour)
print(time_utc_now.minute)
print(time_utc_now.second)
print(time_utc_now.microsecond)
print(time_utc_now.tzinfo)

# 17.14 using timestamps
import math         # included for the math.floor() method
d_now = datetime.datetime.now()

tstamp = math.floor(datetime.datetime.timestamp(d_now))

print(d_now)
print(tstamp)

# 17.15 checking multiple timestamps
d_now = datetime.datetime.now()
now_stamp = datetime.datetime.timestamp(d_now)
print(d_now)
print(now_stamp)
print("-" * 30)

for ctr in range(0,10):
    for ctr2 in range(0, 1000000):
        x = 1       # doing something to take some time...
        x = x + 1
        print(".")

d_later = datetime.datetime.now()
later_stamp = datetime.datetime.timestamp(d_later)

print(d_later)
print(later_stamp)

print("-" * 30)
print(later_stamp - now_stamp)

# 17.16 arithmetic and dates
print(datetime.datetime.now())

# add one day to the current datetime
d1 = datetime.datetime.now() + datetime.timedelta(days = 1)
print(d1)

# subtract 4 weeks from the current datetime
d2 = datetime.datetime.now() - datetime.timedelta(weeks = 4)
print(d2)

# add one hour to the current datetime
d3 = datetime.datetime.now() +  datetime.timedelta(minutes = 60, hours = 1)
print(d3)

# 17.17 calculating the number of days between two dates
d_now = datetime.datetime.now()
d_other = datetime.datetime(2021,1,1)

print(d_now)
print(d_other)

days_passed = d_now - d_other
print(days_passed)
print(days_passed.days)

# 17.18 what's the date
year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: "))

d1 = datetime.datetime(year,month,day)
dnow = datetime.datetime.now()

days_passed = dnow - d1

if days_passed.days < 0:
    past_date = dnow + datetime.timedelta(days_passed.days)
    print("That date is " + str(abs(days_passed.days)) + " days in the future. " + str(abs(days_passed.days)) + " days ago, the date was " + str(past_date.date()) + ".")
elif days_passed.days > 0:
    future_date = dnow + datetime.timedelta(days_passed.days)
    print("That date was " + str(abs(days_passed.days)) + " days ago. In " + str(abs(days_passed.days)) +  " days, the date will be " + str(future_date.date()) + ".")
elif days_passed.days == 0:
    future_date = dnow + datetime.timedelta(weeks = 26)
    print("That's today! In six months, the date will be " + str(future_date.date()) + ".")

# 17.19 showing the date without the time 
time_today = datetime.date.today() # calculates the current date
print(time_today)
print(time_today.year)
print(time_today.month)
print(time_today.day)

# 17.20 days until Christmas
dnow = datetime.date.today()
christmas = datetime.date(dnow.year,12,25)

days_until = christmas - dnow

print("Today is: ", dnow)
print("Christmas is just " + str(days_until.days) + " away!")

# 17.21 using only time without a date
# we create a time object, for 1:45:30 pm, using 24-hour time format
t = datetime.time(13,45,30)
print(t)
print(type(t))

current_time = datetime.datetime.now().time()
print(current_time)
print(type(current_time))

# 17.22 time of day greeting
noon = datetime.time(12,00,00)
current_time = datetime.datetime.now().time()

if current_time >= noon:
    print("Good afternoon!")
elif current_time < noon:
    print("Good morning!")

while True:
    user_input = input("Would you like to enter a time? [Type quit to exit] ")
    if user_input.lower() == 'quit':
        break
    elif user_input.lower() == 'yes':
        user_input_time = input("Enter a time [HH:MM:SS format]: ")
        time_split = [int(i) for i in user_input_time.split(":")]
        user_time = datetime.time(time_split[0],time_split[1],time_split[2])
        if user_time >= noon:
            print(str(user_time) + " is in the afternoon.")
        elif user_time < noon:
            print(str(user_time) + " is in the morning.")