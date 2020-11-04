import calendar
# print(">>>>>>>>>> Leap Year Calculator <<<<<<<<<<")
# y1 = int(input('Enter First Year: '))
# y2 = int(input('Enter Second Year: '))
# leaps = calendar.leapdays(y1, y2)
# print('Number of leap years between', y1, 'and', y2, 'is: ', leaps, ' years')

# year = int(input('Enter the year to display: '))
# print(calendar.prcal(year))

# cal = calendar.TextCalendar(calendar.FRIDAY)
# for i in cal.itermonthdays(2021, 1):
#     print(i)

# for name in calendar.month_name:
#     print(name)
# for name in calendar.day_name:
#     print(name)

# with open("C:/Users/amirb/Desktop/calendar_module/calendar.html", "w") as cal:
#     c = calendar.HTMLCalendar(calendar.SUNDAY)
#     cal.write(c.formatmonth(2020, 12))

year = int(input('Enter the year to display as a webpage: '))
with open("C:/Users/amirb/Desktop/calendar_module/yearly_calendar.html", "w") as cal:
    cal.write(calendar.HTMLCalendar(calendar.SUNDAY).formatyear(year))
