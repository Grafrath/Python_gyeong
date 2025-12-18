print('\n======= while문 =======')


'''
while 조건식:
    실행할 코드

조건식이 True인 동안 반복 실행
조건이 False가 되면 반복 종료
'''


print('\n======= 예제 1 =======\n')

i = 1

while i <= 5:
    print(i)
    i += 1




print('\n======= 예제 2 =======\n')


sleep = 0 
i = 0

while sleep < 10:
    sleep = sleep + 1
    i = i + 1
    print(f"잠을 {sleep}시간째 자고 있습니다.")
    print(f"도둑이 {i}회 들었습니다.")
    if sleep == 10:
        print("잡았다 요놈!!!")





print('\n======= 예제 3 =======\n')


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """



number = 0
while number != 4:
    print(prompt)
    number = int(input())





# ======= 로또 생성 =======
# while, random.randint, set 사용

import random

lotto_numbers = set()  # 빈 집합 생성
while len(lotto_numbers) < 6:
    number = random.randint(1, 45)  # 1~45 사이 랜덤 숫자
    lotto_numbers.add(number)        # 집합에 추가 (중복 자동 제거)

print(lotto_numbers)