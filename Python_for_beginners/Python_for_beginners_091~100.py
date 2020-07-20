# 091
inventory = {"메로나": [300, 20],
             "비비빅": [400, 3],
             "죠스바": [250, 100]}
print(inventory)

# 092
print(inventory["메로나"][0], "원")

# 093
print(inventory["메로나"][1], "개")

# 094
inventory["월드콘"] = [500, 7]
print(inventory)

# 095
icecream = {'월드콘': 2000, '보석바': 1000, '바밤바': 1200, '메로나': 500}
ice = list(icecream.keys())
print(ice)

# 096
price = list(icecream.values())
print(price)

# 097
print(sum(icecream.values()))

# 098
new_product = {'팥빙수': 3000, '망고빙수': 5000}
icecream.update(new_product)
print(icecream)

# 099
keys = ("사과", "복숭아", "바나나")
value = (300, 250, 400)
res = dict(zip(keys, value))
print(res)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
res = dict(zip(date, close_price))
print(close_price)