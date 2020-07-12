# string

# 021
letters = 'python'
print(letters[0], letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[-4:])

# 023
odd_string = "홀짝홀짝홀짝"
print(odd_string[::2])  #':'를 예제와 같이 2개를 사용하면 step을 n개씩 건너뛴다는 의미를 가진다

# 024
string = "PYTHON"
print(string[::-1])     # 반대 순서대로 출력된다

# 025
phone_num = "010-1111-2222"
phone_num = phone_num.replace("-", " ")
print(phone_num)

# 026
phone_num = "010-1111-2222"
phone_num = phone_num.replace('-', '')
print(phone_num)

# 027
url = "https://tbear18.github.io"
url = url.split('.', 2)
print(url[-1]) 

# 028
# lang = 'python'
# lang[0] = 'P'
# print(lang)     # 결과: 문자열은 수정이 안 되기 때문에 Error가 난다

# 029
string = 'abcdefg847awdfacava'
string = string.replace('a', 'A')
print(string)

# 030
string = 'abcd'
print(string.replace('b', 'B'))     # aBcd 출력
print(string)   # abcd가 그대로 출력 
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴
# abcd가 그대로 출력 