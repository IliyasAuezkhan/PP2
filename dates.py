# 1 example

import datetime

x = datetime.datetime.now()
print(x) #output current time

# 2 example

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) # week day name

# 3 example

import datetime

x = datetime.datetime(2020, 5, 17) #also can be added to time

print(x) #2020-05-17 00:00:00

# 4 example

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) # display the name ofthe month

# Exercises
# 1

import datetime
x = datetime.datetime.now()
delta = datetime.timedelta(days = 5)
print(x - delta)

# 2

import datetime
x = datetime.datetime.now()
yes = x - datetime.timedelta(days = 1)
tom = x + datetime.timedelta(days = 1)

# 3

import datetime
x = datetime.datetime.now()
res = x.replace(microseconds = 0)
print(res)

# 4
import datetime
date1 = datetime.datetime(2026, 2, 20, 10, 0, 0)
date2 = datetime.datetime(2026, 2, 24, 12, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)