# 241, 242
import datetime
import time
import os
import numpy

now = datetime.datetime.now()
print(now, type(now))

# 243
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

# 244
print(now.strftime("%H:%M:%S"))

# 245
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

# 246
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 248
ret = os.getcwd()
print(ret, type(ret))

# 249
# 이름 바꾸기
# os.rename("", "")

# 250
for i in numpy.arange(0, 5, 0.1):
    print(i)

