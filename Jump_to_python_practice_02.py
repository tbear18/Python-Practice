# Q1
국어 = 80
영어 = 75
수학 = 55
mean = (국어 + 영어 + 수학) / 3
print(mean)

# Q2
num = 13
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# Q3
number = "881120-1068234"
front = number[:6]
end = number[7:]
print(front, end)

# Q4
print(number[7])

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6
array = [1, 3, 5, 4, 2]
array.sort()
array.reverse()
print(array)

# Q7
a = ['Life', 'is', 'too', 'short']
res = " ".join(a)
print(res)

# Q8
t = (1, 2, 3)
t += (4,)
print(t)

# Q9
a = dict()
print(a)
# 정답은 3번, a[[1]] = 'python'
# dictionary key는 mutable(변하는) 값을 사용할 수 없다. [1]은 list

# Q10
a = {'A':90, 'B':80,'C':70}
print(a.pop('B'))

# Q11
a = {1, 1, 1, 2, 2, 3, 3, 4, 4, 5}
s = set(a)
l = list(s)
print(l)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
# 결과는 b도 바뀐다. -> 모두 동일한 list의 객체를 가리키고 있다.