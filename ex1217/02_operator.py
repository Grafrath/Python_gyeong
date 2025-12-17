print("\n======= 기본 연산자 =======")
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # 0.75
print(a ** b)   # 81    a의 b제곱
print(a % b)    # 3     a 를 b로 나눈 나머지

print(7 / 4)   # 7 나누기 4
print(7 // 4)  # 7을 4로 나눈 몫
print(7 % 4)   # 7을 4로 나눈 나머지


print("\n======= 복합 연산자 =======")

a = 1
a = a + 1  # a += 1 과 같은식
print(a)   # 2

b = 1
b += 1
print(b)   # 2

c = 1
c -= 1
print(c) # 0

# +=, -=, *=, /=, //=, %=, **=
# 각자 해보기

d = 10
d += 5
print(d)

d -= 3
print(d)

d *= 1.67
print(d)

d /= 2
print(d)

d //= 2
print(d)

d %= 10
print(d)

d **= 2
print(d)