import calendar
y = int(input("Δωστε χρονολογία: "))
m = int(input("Δωστε τον μήνα : "))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(y, m))

