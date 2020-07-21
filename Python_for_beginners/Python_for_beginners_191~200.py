# 191
data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
    for col in row:
        print(col * 1.00014)

# 192
for row in data:
    for col in row:
        print(col * 1.00014)
    print("----")

# 193
arr = []
for row in data:
    for col in row:
        arr.append(col * 1.00014)
print(arr)

# 194
arr = []
for row in data:
    sub = []
    for col in row:
        sub.append(col * 1.00014)
    arr.append(sub)
print(arr)