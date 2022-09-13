import jdatetime
import datetime
import pytz
from persiantools.jdatetime import JalaliDate, JalaliDateTime

# ------------------- Testing Jdatetime -------------------
# test = str(jdatetime.datetime.now())
# test2 = str(jdatetime.date.today())
# date = test.split(" ")
# print(date)

# ------------------- 2023 Christmas Shamsi -------------------
# shamsi = jdatetime.date.fromgregorian(day=25,month=12,year=2022)
# print(shamsi)

# ------------------- Datetime -------------------
# print(datetime.datetime.now())

# ------------------- PersianTools Weekday -------------------
print(JalaliDateTime(1369, 7, 1, 14, 0, 10, 0, pytz.utc).strftime("%c"))
