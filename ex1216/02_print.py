print('\n============ 기본 출력 ============')

print('hello, python')
print('Hi Python')
print(123)
print(3.14)
print(True)

print('\n============ 한번에 여러값 출력 ============')

print('나이:',20)
print('이름:', "철수", '점수:', 95)

print('\n============ 줄바꿈 ============')

print('첫 줄')
print('둘째 줄')

print('\n============ 이어쓰기 ============')

print('안녕', end=" ")
print('파이썬')

print('A', end="")
print('B', end="")
print('C')
ㅁ
print('\n============ sep, end  ============')

print(1,2,3)
print(1,2,3, sep=",")
print(1,2,3,sep="/")

print('\n============ 변수 출력  ============')

age = 20
name = '민수'

print(age)
print(name)
print("이름:", name, "나이:", age)

print('\n============ 연산 결과  ============')

print(10+5)
print(10-5)
print(10*3)
print(10/2)

print('\n============ 더하기(+) 콤마(,) ============')

print('홍'+'길'+'동')
print('홍','길','동')
print(3, 4)
print(3+4)
# print('홍'+4)
print('홍', 5)

# print("나이: " + age)   # TypeError

print("나이:", age)
print("나이: " + str(age))

print('\n============ 포맷팅 ============')

age = 25
name = '영희'

print(f'이름은 {name}이고 나이는 {age}살입니다.')
print(f'내년 나이는 {age+1}살입니다.')

print('\n============ 여러줄 출력 ============')

print("""안녕하세요
파이썬 수업입니다
print 연습 중""")

print('\n============ 이스케이프 코드 ============')

print("줄바꿈\n다음줄")
print("탭\t탭")
print("따옴표: \"파이썬\"")
print("역슬래시: \\")

print('\n============ 빈줄 출력 ============')

print("아래 빈 줄 있음")
print()
print("위에 빈 줄 있음")

#====================================

# Hello, Python!을 출력하시오.
# 본인의 이름을 출력하시오. (문자열)
# 100을 출력하시오. (정수)
# 3.14를 출력하시오. (실수)
# True를 출력하시오. (불린)

# 나이: 20 형태로 출력하시오.
# 1 2 3 4 5를 한 줄로 출력하시오.
# 1,2,3,4,5를 한 줄로 출력하시오. (sep 사용)
# 2025-12-15를 한 줄로 출력하시오. (sep 사용)
# A B C를 한 줄로 출력하시오. (sep 사용)
# A B C를 한 줄로 출력하시오. (end 활용)

# 변수 name에 본인 이름을 저장하고 출력하시오.
# 변수 a=10, b=3일 때, 합/차/곱/나눗셈 결과를 각각 출력하시오.

# 변수 price=12000일 때 "가격은 12000원입니다." 를 출력하시오. 
# x=7일 때 x의 제곱은 49입니다.를 출력하시오. 


# 다음의 학원 게시글을 이쁘게 표시하시오.

title = "학원 공지"
date = "2025-12-15"
msg1 = "수업 시간: 18:00 ~ 20:00"
msg2 = "준비물: 필기구, 노트"
msg3 = "숙제: print() 실습 20문제"

print('hello, Python!')
print('정도경')
print(100)
print(3.14)
print(True)

print('나이:',20)
print(1,2,3,4,5)
print(1,2,3,4,5, sep=",")
print(2025, 12, 15, sep="-")
print('A','B','C', sep=" ")
print('A', end=" ")
print('B', end=" ")
print('C')

name = '도경'
a, b, x, price = 10, 3, 7, 12000

print(name)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(f'가격은 {price}원입니다.')
print(f'X의 제곱은 {x**2}입니다.')


print()
print()

print('=======', title, '=======')
print()
print('              ',date)
print()
print(msg1)
print()
print(msg2)
print()
print(msg3)