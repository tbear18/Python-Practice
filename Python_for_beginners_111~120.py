# 111
user = input("입력: ")
print(user * 2)

# 112
num = input("숫자를 입력하세요: ")
print(int(num) + 10)

# 113
num = input("")
if int(num) % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 114
user = input("입력값: ")
num = 20 + int(user)
if num > 255:
    print(255)
else:
    print(num)

# 115
user = input("입력값: ")
num = int(user) - 20
if num > 255:
    print(255)
elif num < 0:
    print(0)
else:
    print(num)

# 116
time = input("현재시간: ")
if time[-2:] == "00":
    print("정각입니다.")
else:
    print("정각이 아닙니다.")

# 117
fruit = ["사과", '오렌지', "바나나"]
과일 = input("좋아하는 과일은?")
if 과일 in fruit:
    print("정답입니다.")
else:
    print("정답이 아닙니다.")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "Samsung", "LG"]
종목 = input("종목명: ")
if 종목 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

# 119
season = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
계절 = input("내가 좋아하는 계쩔은?")
if 계절 in season:
    print("정답")
else:
    print("오답")

# 120
과일 = input("내가 좋아하는 과일은?")
if 과일 in season.values():
    print("정답")
else:
    print("오답")