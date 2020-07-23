# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


# Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# Q3
all([1, 2, abs(-3)-3]) # False
chr(ord('a')) == 'a' # True

# Q4
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

# Q5
print(hex(234))
print(int('0xea', 16))

# Q6
print(list(map(lambda a: a * 3, [1, 2, 3, 4])))

# Q7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a), min(a))

# Q8
print(round(17 / 3, 4))

# Q9
import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)

# Q10
import os
os.chdir("D:\Study\GitHub\Python-Practice\Jump_to_python_practice")
result = os.popen("dir")
print(result.read())

# Q11
import glob
print(glob.glob("D:\Study\GitHub\Python-Practice\Jump_to_python_practice/*.py"))

# Q12
import time
time.strftime("%Y/%m/%d %H:%M:%S")   # %Y:년, %m:월, %d:일, %H:시, %M:분, %S:초

# Q13
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)

print(result)