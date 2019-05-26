import datetime
year_1 = int(input('Enter a year '))
month_1 = int(input('Enter a month '))
day_1 = int(input('Enter a day '))
date1 = datetime.date(year_1, month_1, day_1)
year_2 = int(input('Enter a year '))
month_2 = int(input('Enter a month '))
day_2 = int(input('Enter a day '))
date2 = datetime.date(year_2, month_2, day_2)
if date1>date2:
    date3=date1-date2
else:
    date3=date2-date1
print(date3)