# 151
arr = [3, -20, -3, 44]
for var in arr:
    if var < 0:
        print(var)

# 152
arr = [3, 100, 23, 44]
for var in arr:
    if var % 3 == 0:
        print(var)

# 153
arr = [13, 21, 12, 14, 30, 18]
for var in arr:
    if var % 3 == 0 and var < 20:
        print(var)

# 154
arr = ["I", "study", "python", "language", "!"]
for var in arr:
    if len(var) >= 3:
        print(var)

# 155
arr = ["A", "b", "c", "D"]
for var in arr:
    if var.isupper():
        print(var)

# 156
arr = ["A", "b", "c", "D"]
for var in arr:
    if var.islower():
        print(var)

# 157
arr = ['dog', 'cat', 'parrot']
for var in arr:
    print(var[0].upper() + var[1:])

# 158
arr = ['hello.py', 'ex01.py', 'intro.hwp']
for var in arr:
    split = var.split(".")
    print(split[0])

# 159
arr = ['intra.h', 'intra.c', 'define.h', 'run.py']
for var in arr:
    split = var.split(".")
    if split[1] == "h":
        print(var)

# 160
arr = ['intra.h', 'intra.c', 'define.h', 'run.py']
for var in arr:
    split = var.split(".")
    if split[1] == "h" or split[1] == "c":
        print(var)
