# 141
arr = [100, 200, 300]
for var in arr:
    print(var * 10)

# 142
arr = ["chicken", "coke", "beer"]
for food in arr:
    print("오늘의 메뉴:", food)
    # print("오늘의 메뉴: " + 메뉴)

# 143
arr = ["SKT", "KT", "LG"]
for var in arr:
    print(len(var))

# 144
arr = ["SKT", "KT", "LG"]
for var in arr:
    print(var, len(var))

# 145
arr = ["SKT", "KT", "LG"]
for var in arr:
    print(var[0])

# 146
arr = [1, 2, 3]
for var in arr:
    print("3 x %d" % var)
    # print("3 x", var)
    # print("3 x " + str(var))

# 147
arr = [1, 2, 3]
for var in arr:
    print("3 x ", var, "=", 3 * var)
    # print("3 x {} = {}".format(var, 3 * var))

# 148
arr = ["a", "b", "c", "d"]
for var in arr[1:]:
    print(var)

# 149
# list slicing
arr = ["a", "b", "c", "d"]
for var in arr[::2]:   # [start:end:step]
    print(var)
# step이 양수일 때: 오른쪽으로 step만큼 이동하면서 가져온다.
# step이 음수일 때: 왼쪽으로 step만큼 이동하면서 가져온다.

# 150
arr = ["a", "b", "c", "d"]
for var in arr[::-1]:
    print(var)
