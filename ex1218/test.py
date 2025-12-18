import random

lonum = set()

while len(lonum) < 6:
    num = random.randint(1, 45)
    lonum.add(num)

print(sorted(list(lonum)))

# 1부터 100까지의 합 명확한 범위면 for
print(sum(i for i in range(1,100)))

# 1~100 중 3의 배수
num = 0
while True :
    num += 1
    if num%3 == 0 :
        print(num)
    if num == 100 : break

# 숫자 맞추기 랜덤
while False : #한번에 맞출떄까지 반복
    num = random.randint(1, 10)
    ans = input("숫자를 입력하세요: ")
    if int(ans) == num :
        print("맞췄습니다.")
        break
    print(f'답은 {num}')

num = random.randint(1, 100)

while False :
    ans = input("숫자를 입력하세요: ")
    if int(ans) == num :
        print("맞췄습니다.")
        break
    elif int(ans) > num :
        print('down.')
    else :
        print('up')

x = 1
while x < 10 :
    for y in range(2,10) :
        print(f'{x} x {y} = {x*y}')
    x += 1
    print()

for x in range(1,10) :
    for y in range(2,10) :
        print(f'{y} x {x} = {x*y}', end='\t')
    print()