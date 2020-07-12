# list

# 051
movie_rank = ["venom", "spider man", "avengers"]

# 052
movie_rank.append("thor")
print(movie_rank)

# 053
movie_rank.insert(1, "hulk")
print(movie_rank)

# 054
del movie_rank[3]
print(movie_rank)

# 055
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 056
lang1 = ["C", "C++", "Java"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 057
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ",max(nums))
print("min: ",min(nums))

# 058
print(sum(nums))

# 059
cook = ["pizza", "gimbab", "chicken", "gimchi", "pasta", "beer"]
print(len(cook))

# 060
average = sum(nums) / len(nums)
print(average)