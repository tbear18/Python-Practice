# 121
user = input("알파벳 입력: ")
if user.islower():
    print(user.upper())
else:
    print(user.lower())

# 122
score = input("점수 입력: ")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")

# 123
환율 = {"달러": 1167,
      "엔": 1.096,
      "유로": 1268,
      "위안": 171}
money = input("입력: ")
num, currency = money.split()
print(float(num) * 환율[currency], "원")

# 124
num1 = input("input 1: ")
num2 = input("input 2: ")
num3 = input("input 3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

a = [num1, num2, num3]
print(max(a))

# 125
number = input("휴대폰 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

# 126
zip_code = input("우편번호: ")
zip_code = zip_code[:3]
if zip_code in ["010", "011", "012"]:
    print("강북구")
elif zip_code in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

# 127
num = input("주민등록번호: ")
num = num.split("-")[1]
if num[0] == "1" or num[0] == "3":
    print("남자")
else:
    print("여자")

# 128
num = input("주민등록번호: ")
num = num.split("-")[1]
if 0 <= num[1:3] <= 8:
    print("서울")
else:
    print("서울X")

# 129
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
