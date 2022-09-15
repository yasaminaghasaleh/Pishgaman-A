import jdatetime
from persiantools.jdatetime import JalaliDateTime

now = str(jdatetime.datetime.now())

print(now.split(" ")[0])
print(now.split(" ")[1][:5])

# print(type(JalaliDateTime.now()))
