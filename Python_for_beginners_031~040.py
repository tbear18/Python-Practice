# 031
a = "3"
b = "4"
print(a + b) # 34

# 032
print("Hi" * 3) # HiHiHi

# 033
print("-" * 80)

# 034
t1 = 'python'
t2 = 'c'
print((t1 + " " + t2 + " ") * 4)

# 035
name1 = "민수"
age1 = 10
name2 = "현수"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 036
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 037
# f-string
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 038
comma = "3,423,565,64"
comma = int(comma.replace(",", ""))
print(comma, type(comma))

# 039
slicing = "2020/07(ABcDe) (모니터)"
print(slicing[:7])

# 040
data = "    SAMSUNG     "
data = data.strip()
print(data)