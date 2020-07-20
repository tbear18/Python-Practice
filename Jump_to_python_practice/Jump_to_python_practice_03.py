# Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")   # error
elif "python" in a and "you" not in a: print("python")  # error
elif "shirt" not in a: print("shirt")   # shirt
elif "need" in a: print("need")         # need
else: print("none")

# Q2
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

# Q3
i = 0
while True:
    i += 1
    if i > 5:
        break
    print('*' * i)

# Q4
for i in range(1, 101):
    print(i)

# Q5
A = [70, 65, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in A:
    sum += score

mean = sum / len(A)
print(mean)

# Q6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)

# list comprehension
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)