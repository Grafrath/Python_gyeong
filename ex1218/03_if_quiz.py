'''
타 언어의 else if의 경우 파이썬은 elif 로 표현한다
가끔 하는 실수라서 따로 메모함
'''

pocket = ['paper', 'cellphone', 'money']
print("\n======== Sample ========\n")

if (True) :
    print("이 문장은 참입니다.")
else :
    print("이 문장은 참입니다.")

if (False) :
    print("이 문장은 참이 아닙니다.")
else :
    print("이 문장은 참이 아닙니다.")

print()

'''
비교 연산자를 이용하는 순간 반환되는 값은
true or false로 고정된다.
'''

x = 3
y = 2

print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)

print()

'''
논리 연산자, 여러 비교(조건)을 조합하거나 반전할때 사용 하는 조건이다
ex) 키가 160보다 크면서 180보단 작아야한다.
'''

money = 2000
card = True

if money >= 3000 or card:
    print("택시를 탄다")
else:
    print("걸어간다")

if money >= 3000 and card:
    print("택시를 탄다")
else:
    print("걸어간다")

if card:
    print("택시를 탄다")
else:
    print("걸어간다")

if not card:
    print("택시를 탄다")
else:
    print("걸어간다")
print()

'''
in / not in 해당 요소가 리스트, 튜플, 문자열등
배열형태에 포함되어 있는지 물어보는 형식이며 기본적으로 in,
논리 연산자인 not을 이용하여 포함되지 않는지를 물어본다.
'''

sample = {"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}

print("귀도" in sample)
print("파이썬" in sample)
# 딕셔너리의 경우 키로 값을 조회하는 형태다 보니 값은 false 키는 true가 나옴
print()

'''
pass조건문에서 결과시 진행하는부분없이 지나가게 해줌,
예외를 처리하거나, 실행하고싶은게 없을때 넣어줌
...으로 대체 가능함. < 이부분은 당장 쓸 내용이 없어서 넣어둔걸로 확실하게 인지가능

if 'money' in pocket:
else:
    print('걸어가라')

참일때 실행하는 부분이 없어서 에러남
'''

if 'money' in pocket:
    ...
else:
    print('걸어가라')

#주머니에 돈이 있으면 택시, 돈이 없는데 카드가 있으면 택시, 둘다 없으면 걸어간다.
if 'money' in pocket :
    print("택시를 탄다")
else:
    if card :
        print("택시를 탄다")
    else:
        print("걸어간다")
print()

#2중 조건 표현식
# 3항 연산자와 비슷함(중첩되는 요소여부차이)

score1 = 78
score2 =95

grade = "A" if score1 >= 90 else "B" if score1 >= 80 else "C"
print(grade)
print("A" if score1 >= 90 else "B" if score1 >= 80 else "C")
grade = "A" if score2 >= 90 else "B" if score2 >= 80 else "C"
print(grade)
print()

''' 
카페 주문 시나리오

가지고 있는 돈(money)과 쿠폰(coupon) 여부에 따라 음료를 주문합니다.

돈이 5000원 이상이면 "아메리카노 주문", 돈이 부족하지만 쿠폰이 있으면 "아메리카노 주문", 둘 다 아니면 "집에서 물 마시기"를 출력하세요.

if / elif / else 문 사용.
'''
money = 4500
coupon = False

if money >= 5000 :
    print("아메리카노 주문")
elif coupon :
    print("아메리카노 주문")
else :
    print("물이나 마셔라")
print()

'''
시험 결과 판별

학생 점수(score)를 기준으로 등급을 결정합니다.

90 이상 "A", 80 이상 "B", 70 이상 "C", 그 외 "F"를 출력하도록 합니다.

2중 조건부 표현식(삼항 연산자) 사용.
'''

score = 90
print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F")
print()

'''
영화관 입장 시나리오

나이(age), 돈(money), 티켓(has_ticket) 여부에 따라 영화관 입장 가능 여부를 판단합니다.

티켓이 있으면 "입장 가능", 없으면 나이가 19세 이상이고 돈이 10000원 이상이면 "현장 구매 후 입장", 그 외 "입장 불가".

중첩 if 문과 and 논리 연산자 사용.
'''

has_ticket = False
money = 10500
age = 19

if has_ticket :
    print("입장 가능")
else :
    if age>=19 and money >= 10000 :
        print("현장 구매 후 입장")
    else :
        print("입장 불가")