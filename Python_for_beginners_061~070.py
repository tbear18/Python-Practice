# 061
price = ['20181212', 134, 140, 135, 160]
print(price[1:])

# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 063
print(nums[1::2])

# 064
print(nums[::-1])

# 065
enterprise = ['samsung', 'lg', 'naver']
print(enterprise[0], enterprise[2])

# 066
print(" ".join(enterprise))

# 067
print("/".join(enterprise))

# 068
print("\n".join(enterprise))

# 069
string = "samsung/lg/naver"
enterprise = string.split("/")
print(enterprise)

# 070
data = [2, 4, 6, 1, 5, 9, 7, 3]
data.sort()
print(data)
data2 = sorted(data)
print(data2)