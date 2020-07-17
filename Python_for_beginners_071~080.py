# tuple

# 071
my_variable = ()

# 072
movie_rank = ("헐크", "어바웃타임", "드래곤 길들이기")

# 073
number_one = (1, )

# 074
t = (1, 2, 3)
# t[0] = 'a'
# tuple은 원소 값 변경 불가

# 075
t = 1, 2, 3, 4
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작한다.

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

# 077
interest = ('samsung', 'lg', 'skt')
print(list(interest))

# 078
interest = ['samsung', 'lg', 'skt']
print(tuple(interest))

# 079
temp = ('apple', 'banana', 'mango')
a, b, c = temp
print(a, b, c)

# 080
data = tuple(range(2, 100, 2))
print(data)