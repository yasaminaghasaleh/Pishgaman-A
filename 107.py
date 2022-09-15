import pytz
from persiantools.jdatetime import JalaliDate, JalaliDateTime

date = JalaliDateTime(1369, 7, 1, 14, 0, 10, 0, pytz.utc).strftime("%c")
date = date.split(" ")

print(date[0])
