'''# 각 요소에 3 곱하기
a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num*3)

print(result)  # [3, 6, 9, 12]




print('\n======= 리스트 컴프리헨션 =======')
# 각 요소에 3 곱하기

a = [1, 2, 3, 4]

result = [num * 3 for num in a]

print(result) # [3, 6, 9, 12]
print()






# 짝수에만 3 곱하기
a = [1, 2, 3, 4]

result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]
print()

# [결과 for 항목 in 리스트(튜플) if 문 ]
# for문을 2개 이상 사용하는 것도 가능 하다.


result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)




print("\n======= break =======\n")
for i in range(10):
    print(i, end=' ')
    if i == 5:
        break
print()

print("안녕히 주무세요")




print("\n======= for-else 문 =======\n") # for문이 정상종료 되었을때만 else문 작동
for i in range(5):
    print(i)
else:
    print("for문 정상종료.")

print()

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("for문 정상종료???")

print("\n======= enumerate 함수 =======\n")

fruits = ['apple', 'banana', 'orange']

for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')

print()

for i, fruit in enumerate(fruits, 1):  # 1부터 시작
    print(f'{i}: {fruit}')

print()

print("\n======= zip 함수 =======\n")

names = ['홍길동', '김철수', '이영희']
scores = [85, 93, 56]

a = zip(names, scores)
print('\na 출력')
print(a)

print('\nlist(a) 첫번째 출력')
print(list(a))

print('\nlist(a) 두번째 출력')
print(list(a))

print()

names = ['홍길동', '김철수', '이영희']
scores = [85, 93, 56]

# [('홍길동', 85), ('김철수', 93), ('이영희', 56)]
for name, score in zip(names, scores):
    print(f'{name}: {score}점')

print()

print('\n======= 개수가 안맞는 경우 =======\n')

names = ['홍길동', '김철수', '이영희', '박영수']
scores = [85, 93, 56]

for name, score in zip(names, scores): # 개수가 안맞을 경우 무시됨.
    print(f'{name}: {score}점')

print()

print('\n======= zip_longest =======\n')

# zip_longest 임포트!
from itertools import zip_longest

for name, score in zip_longest(names, scores, fillvalue="점수 없음"): 
    print(f'{name}: {score}')

print()

print('\n======= zip 실습 =======')

names = ['홍길동', '김철수', '이영희']
korean = [85, 93, 56]
english = [90, 100, 95]

# 홍길동 : 국어 85점, 영어 90점

for name, korean, english in zip_longest(names, scores, english): 
    print(f'{name} : 국어 {korean}점, 영어 {english}점')

# 피라미드
for i in range(1,9,2) :
    print(f"{i * '*':^13}")
print()
'''

# 다이아
'''
for i in range(1, 11 + 1, 2):
    print(f"{'*'*i:^11}")

for i in range(11 - 2, 0, -2):
    print(f"{'*' * i:^11}")
print()'''

for i in range(-5,6):
    stars = 11 - abs(i)*2
    star_count = " ".join("*" * stars)
    print(f"{star_count:^21}")

'''
# 선택정렬
li = [7, 2, 5, 8, 9, 1, 3, 6, 4]
print(li)
n=len(li)
for i in range(n):
        min= i
        for j in range(i + 1, n):
            if li[j] < li[min]:
                min = j
        li[i], li[min] = li[min], li[i]
        print(li)

print(li)
print()

# 버블정렬
li = [64, 25, 12, 22, 11]
print(li)
n=len(li)
for i in range(n):
        for j in range(0, n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print(li)
print(li)
print()
'''