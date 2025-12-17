print('\n======= 문자열 포매팅2 =======')


print("I eat {0} apples".format(3))

print("I eat {0} apples".format("five"))

number = 7
print("I eat {0} apples".format(number))



number = 10
day = "three"

print("I ate {0} apples, so I was sick for {1} days.".format(number, day))

print("I ate {number} apples, so I was sick for {day} days.".format(number=10, day=3))

print("I ate {0} apples, so I was sick for {day} days.".format(number, day=3))




print("\n======= 정렬1 =======")

print("{0:<10}".format("hi"))

print("{0:>10}".format("hi"))

print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))

print("{0:!<10}".format("hi"))
print()

y = 3.141592
print("{0}".format(y))
print("{0:0.3f}".format(y))
print("{0:10.3f}".format(y))


print("\n======= 문자열 포매팅3 =======")

name = '홍당무'
age = 20

print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age + 1}살이 됩니다.')


# 딕셔너리 {키:밸류}

# d = {'name':'홍당무', 'age':30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
# print()

print("\n======= 정렬2 =======")

print(f'{"hi":<10} 으하하')
print(f'{"hi":>10} 으하하')
print(f'{"hi":^10} 으하하')
print(f'{"hi":=^10} 으하하')
print(f'{"hi":!>10} 으하하')
print()


y = 3.141592
print(f'{y:0.4f} 으하하')
print(f'{y:10.4f} 으하하')
print()

print('난 2000000000원이 필요해')
print(f'난 {2000000000:,}원이 필요해')



# ======= 문자열 포매팅 실습 =======

# 1번 실습
#   ***cat****
print(f"{"cat":*^10}")

# 2번 실습
pi = 3.141592
#   3.14______
print(f"{pi:_<10.2f}")
#   ______3.14
print(f"{pi:_>10.2f}")

# 3번 실습
# 00042  (5칸 확보하고 나머지 0으로 채우기)
num = 42
print(f"{num:0>5}")

# 4번 실습
a = 7.3 
# ___7.30 (10칸 확보하고 소수점 아래 두자리로)
print(f"{a:_>10.2f}")

# 5번 실습
# 변수, 문자 슬라이싱 등을 사용하여 아래의 결과물과 똑같이 출력하시오
# print() 는 한 번만 쓸 것.

'''
이름    년도    월      일      성별
홍길동  97      03      01      M
'''

info = '970301-1234567홍길동M'
print(f'''
이름    년도    월    일    성별
{info[14:17]}  {info[:2]}      {info[2:4]}    {info[4:6]}    {info[17]}
''')

