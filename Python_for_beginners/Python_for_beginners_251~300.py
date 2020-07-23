# 252 ~ 257

class Human:
    def __init__(self, name, age):
        print("Hi")
        self.name = name
        self.age = age

    def __del__(self):
        print("die")

    def who(self):
        print("이름: {} 나이: {}".format(self.name, self.age))

    def setInfo(self, name, age):
        self.name = name
        self.age = age

areum = Human("Lee", 25)
print(areum.name)
areum.who()
areum.setInfo("Kim", 23)
areum.who()

# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드