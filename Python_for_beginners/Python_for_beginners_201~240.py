# 201
def print_coin():
    print("bitcoin")


# 204
def print_coins():
    for i in range(100):
        print("비트코인")


# 205
# hello() 함수가 정의되기 전에 호출되면 에러
def hello():
    print("Hi")


# 함수 결과 예측하기, 간단한 함수 제작 -> 생략 생소한 문제들만 해결

# 235
def convert_int(string):
    print(int(string.replace(',', '')))


convert_int("1,234,567")
