import datetime
now = datetime.datetime.now()
CurrMth = now.month
CurrND = now.day
CurrDay = 1 
if (CurrDay > 1) :
 Diff = 7 - CurrDay
else :
    Diff = 0
CurrYr = now.year
TillYr = CurrYr + 10
tp = 0
TotalDays = 0
for i in range(CurrYr, TillYr + 1):
    tp = tp + 1
    if i == CurrYr + (4*tp) :
        TotalDays = TotalDays + 366
    else :
        TotalDays = TotalDays + 365

NumbMon = 0
TotalDays = TotalDays - Diff
tp = 0
for i in range(0, TotalDays):
    if (i % 7) == 0 :
        NumbMon = NumbMon + 1
print NumbMon

    

        
    

