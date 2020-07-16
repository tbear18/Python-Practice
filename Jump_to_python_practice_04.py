# Q1
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
# 람다와 조건부 표현식
is_odd = lambda x: True if x % 2 == 1 else False

# Q2
def avg_numbers(*args):
    result = 0
    for i in args:
        res += 1
        return res / len(args)

# Q3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
sum = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % sum)

# Q4
print("you", "need", "python")

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")
with open("test.txt", 'r') as f2:
    print(f2.read())

# Q6
a = input("저장할 내용을 입력하세요:")
f = open("test.txt", 'a')
f.write(a)
f.write('\n')
f.close()

# Q7
f = open('test.txt', 'r')
text = f.read()
f.close()

text = text.replace('java', 'python')

f = open('test.txt', 'w')
f.write(text)
f.close()