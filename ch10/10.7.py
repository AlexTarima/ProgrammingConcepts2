# This program will set the datetime's class date to one variable
# It will then set it to another
# It will then subtract the differences

import datetime

#a
x = datetime.datetime.now()

#b
y = datetime.datetime.now()

#c
print("Datetime object x:", x)
print("Datetime object y:", y)

#d
print("\nDatetime object x attributes:")
print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)
print("Hour:", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)
print("Microsecond:", x.microsecond)

print("\nDatetime object y attributes:")
print("Year:", y.year)
print("Month:", y.month)
print("Day:", y.day)
print("Hour:", y.hour)
print("Minute:", y.minute)
print("Second:", y.second)
print("Microsecond:", y.microsecond)

#e
print("\nComparison results:")
print("x == y:", x == y)
print("x > y:", x > y)
print("x < y:", x < y)

#f
difference = y - x
print(difference)