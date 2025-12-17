print('\n======== 리스트 자료형 ========')

odd = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = []
b = ['life', 'is', 'too', 'short']
c = [1, 2, 'life', 'is']
d = [1, 2, ['life', 'is']]

print('\n======== 리스트 인덱싱 ========\n')

print(odd)
print(odd[0])
print(odd[0]+odd[3])
print(odd[-1])

print('\n======== 이중 리스트 ========\n')

a = [1, 2, 3, ['a', 'b', 'c']]

print(a[0])
print(a[3])
print(a[-1])
print()

print(a[3][1])
print(a[-1][-1])

print('\n======== 다중 리스트 ========\n')

a = [1, 2, ['a', 'b', ['Life', 'is']]]

# Life 를 뽑아 내시오.
print(a[-1][-1][0])
print(a[2][2][0])

print('\n======== 리스트 슬라이싱 ========\n')

a = [1, 2, 3, 4, 5]

print(a[0:2])
print(a[:2])
print(a[2:])
print()

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(a[2:5])
print(a[3][:2])

print('\n======== 리스트 연산 ========\n')

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)  # [1, 2, 3, 4, 5, 6]
print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(a)) # 3

# print(a + 'hi')
# print(a[2] + 'hi')
print(a[2] , 'hi', sep='')
print(str(a[2]) + 'hi')

print('\n======== 리스트 연산 ========\n')

a = [1, 2, 3]

a.append(100)
print(a, '\n')

a.append([7, 9])
print(a, '\n')

a = [1, 4, 3, 2]
print(a, '\n')

a.sort(reverse=1)
print(a, '\n')

a = ['a', 'c', 'b']
a.reverse()
print(a, '\n')

a = [5, 6, 7]
print(a.index(7))
print()

a = [1, 2, 3]
a.insert(0, 4)
print(a, '\n')

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a, '\n')

a.remove(3)
print(a, '\n')

a = [1, 2, 3]
print(a.pop())
print(a, '\n')

a = [1, 2, 3]
print(a.pop(1))
print(a, '\n')

a = [1, 2, 3, 1]
print(a.count(1))
print()

a = [1, 2, 3]
a.extend([4, 5])
print(a)

a = [1, 2, 3]
a = a + [4, 5]
print(a)

b = [6, 7]
a.extend(b)
print(a, '\n')

print('\n======== 퀴즈 ========\n')

#1 숫자 1, 3, 5, 7, 9를 요소로 가지는 리스트를 생성하고 출력하시오.
list = [1, 3, 5, 7, 9]
print(list, '\n')

#2 빈 리스트를 생성하고 출력하시오.
list = []
print(list, '\n')

#3 문자열 'life', 'is', 'too', 'short'를 요소로 가지는 리스트를 생성하고 출력하시오.
list = ['life', 'is', 'too', 'short']
print(list, '\n')

#4 리스트 [10, 20, 30]에서 첫 번째 요소를 출력하시오.
list = [10, 20, 30]
print(list[0], '\n')

#5 리스트 [10, 20, 30]에서 마지막 요소를 출력하시오. (음수 인덱스 사용)
list = [10, 20, 30]
print(list[-1], '\n')

#6 리스트 [1, 2, 3, ['a', 'b', 'c']]에서 문자 'b'를 출력하시오.
list = [1, 2, 3, ['a', 'b', 'c']]
print(list[3][1], '\n')

#7 리스트 [1, 2, ['a', 'b', ['Life', 'is']]]에서 문자열 "Life"를 출력하시오.
list = [1, 2, ['a', 'b', ['Life', 'is']]]
print(list[2][2][0], '\n')

#8 리스트 [1, 2, 3, 4, 5]에서 앞의 두 개 요소만 슬라이싱하여 출력하시오.
list = [1, 2, 3, 4, 5]
print(list[:2], '\n')

#9 리스트 [1, 2, 3, 4, 5]에서 세 번째 요소부터 끝까지 슬라이싱하여 출력하시오.
list = [1, 2, 3, 4, 5]
print(list[2:], '\n')

#10 리스트 [1, 2, 3, ['a', 'b', 'c'], 4, 5]에서 ['a', 'b', 'c']를 슬라이싱하여 출력하시오.
list = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(list[3][:], '\n')

#11 리스트 [1, 2, 3]과 [4, 5, 6]을 더해 하나의 리스트로 출력하시오.
list = [1, 2, 3]
list.extend([4, 5, 6])
print(list, '\n')

#12 리스트 [1, 2, 3]을 3번 반복한 결과를 출력하시오.
list = [1, 2, 3]
for i in list : print(list) #?
print(list*3, '\n') # 둘중 뭘 달라는거지?

#13 리스트 [10, 20, 30, 40]의 길이를 출력하시오.
list = [10, 20, 30, 40]
print(len(list), '\n')

#14 리스트 [1, 2, 3]의 세 번째 요소를 문자열 'hi'와 이어서 출력하시오.
list = [1, 2, 3]
print(list[2] , 'hi', '\n', sep='')

#15 리스트 [1, 2, 3]에서 세 번째 요소를 100으로 수정한 뒤 출력하시오.
list = [1, 2, 3]
list[2] = 100
print(list , '\n')

#16 리스트 [1, 2, 3]에서 두 번째 요소를 삭제한 뒤 출력하시오.
list = [1, 2, 3]
list.pop(1)
print(list , '\n')

#17 리스트 [1, 2, 3]의 맨 뒤에 숫자 99를 추가한 뒤 출력하시오.
list = [1, 2, 3]
list.append(99)
print(list , '\n')

#18 리스트 [4, 2, 3, 1]을 오름차순으로 정렬하여 출력하시오.
list = [4, 2, 3, 1]
list.sort()
print(list , '\n')

#19 리스트 [1, 2, 3, 1]에서 숫자 1의 개수를 출력하시오.
list = [1, 2, 3, 1]
print(list.count(1), '\n')

#20 리스트 [1, 2, 3]에 리스트 [4, 5]를 확장하여 출력하시오. (extend 사용)
list = [1, 2, 3]
list.extend([4, 5])
print(list, '\n')

# =======================================

# 상품 이름
name = ['새우깡', '바나나킥', '양파링', '고래밥', '포카칩']

# 상품 가격
prices = [1200, 1500, 1000, 1800, 2000]

# 판매 개수
quantities = [3, 2, 5, 1, 4]

totalPrice = []

# 총 매출액을 계산하여 아래와 같이 출력하시오

'''
상품명          가격    판매수량        매출금액
================================================
새우깡          1200       3            3600
바나나킥        1500       2            3000
양파링          1000       5            5000
고래밥          1800       1            1800
포카칩          2000       4            8000
================================================
총 매출 금액 = 21400 원
================================================
'''

print('상품명          가격    판매수량        매출금액')
print('================================================')
for i in range(5) :
    print(f'{name[i]:9}',end='')
    print(f'{prices[i]:8}', end='')
    print(f'{quantities[i]:^18}', end='')
    totalPrice.append(prices[i] * quantities[i])
    print(f'{totalPrice[i]:^10}')
print('================================================')
print(f'총 매출 금액 = {sum(totalPrice)} 원')
print('================================================') 