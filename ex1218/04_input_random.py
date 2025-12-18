# ======= 사용자 입력, input 함수 =======

# name = input("\n이름을 입력하세요: ")
# print("안녕하세요,", name)


# a = input("\n숫자를 입력하세요: ")
# print(f'입력한 숫자는 {a}입니다.')
# print(type(a)) # 모든 인풋값은 문자열
# print()


# age = int(a) # 정수로 변환
# print(f'나이는 {age}살 입니다.')
# print(type(age))
# print()



# height = input("\n키를 입력하세요: ")
# height = float(height)
# print(f'키는 {height}cm 입니다.')
# print(type(height))
# print()



# age = int(input("\n나이를 입력하세요: "))
# print(f"내년에는 {age + 1}살 입니다.")
# print()




# # ======= 랜덤모듈 =======

import random


print('\n======= 0 이상 1미만 실수 =======\n')
print(random.random())  # 0.0 <= x < 1.0


print('\n======= 1 이상 10 이하 정수 =======\n')
print(random.randint(1, 10))  # 1 ~ 10


print('\n======= 1 이상 10 미만 정수 =======\n')
print(random.randrange(1, 10))  # 1 ~ 9


print('\n======= 실수 범위 난수 =======\n')
print(random.uniform(1.5, 5.5)) # 실수 범위 난수




print('\n======= 랜덤 선택 (1개) =======\n')
print(random.choice([1, 2, 3, 4, 5])) 
print(random.choice(range(1, 46)))


print('\n======= 랜덤 샘플링 (중복 없음)) =======\n')
print(random.sample([1, 2, 3, 4, 5], 3)) 
print(random.sample(range(1, 46), 6)) 


print('\n======= 셔플링 =======\n')
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)
