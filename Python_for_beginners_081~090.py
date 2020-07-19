# dictionary

# 081
# unpacking
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)

# 082
a, b, *valid_score = scores
print(valid_score)

# 083
a, *valid_score, b = scores
print(valid_score)

# 084
temp = { }

# 085
ice = {"메로나": 1000, "폴라포": 1200, "돼지바": 500}
print(ice)

# 086
ice["죠스바"] = 600
ice["월드콘"] = 1400
print(ice)

# 087
ice = {'메로나': 1000,
       '폴라포': 1200,
       '돼지바': 500,
       '죠스바': 600,
       '월드콘': 1400}
print("메로나 가격: ", ice["메로나"])

# 088
ice["메로나"] = 1300

# 089
del ice["메로나"]
print(ice)

# 090
# dictionary에 없는 key를 사용하여 indexing하면 error를 발생