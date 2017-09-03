import datetime

import calendar
t = datetime.time(1,15,54)

print t

today = datetime.date.today()

print today

one_day = datetime.timedelta(today.day + 1)

print one_day

print today - one_day

print today + one_day

t1 = datetime.time(0,42,19)
t2 = datetime.time(0,42,11)

print t1 > t2

print "parsing date"

format = "%a %b %d %H:%M:%S %Y"

release_date = datetime.datetime(1982,11,30,0,42,19)

print "ISO: ",release_date


s = release_date.strftime(format)

print "strftime ",s

c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(1982,11)

print c.firstweekday