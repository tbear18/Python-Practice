# 101
# bool

# 102
print(3 == 5)
# False

# 103
print(3 < 5)
# True

# 104
x = 4
print(1 < x < 5)
# True

# 105
print((3 == 3) and (4 != 3))
# True

# 106
# print(3 => 4)
# 지원하지 않는 연산자

# 107
if 4 < 3:
    print("Hello World")
# 조건이 만족하지 않기에 출력이 안 된다

# 108
if 4 < 3:
    print("Hello World")
else:
    print("Hi, there")

# 109
if True:
    print('1')
    print('2')
else:
    print('3')
print('4')

# 110
if True:
    if False:
        print('1')
        print('2')
    else:
        print('3')
else:
    print('4')
print('5')