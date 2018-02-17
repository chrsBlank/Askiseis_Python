import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(y, m))

