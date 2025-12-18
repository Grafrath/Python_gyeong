print('\n======= if 문 =======')

money = False

if money:
    print("택시를 타고 간다")
else:
    print("걸어 간다") 

'''
if 조건문:
    수행할_문장
else:
    수행할_문장
'''
print()


if money:
    print("돈 있어서 좋겠다.")
    print("밥 한 번 쏴라!")




print("\n======= 비교연산자 =======")

x = 3
y = 2

print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)



money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")




print("\n======= and/or/not =======")

money = 2000
card = True

if money >= 3000 or card:     # or 이기 때문에 하나만 참이어도 참.
    print("택시를 타고 가라")
else:
    print("걸어가라")



money = 2000
card = True
if money >= 3000 and card:    # and 이기 때문에 둘다 참이어야 참.
    print("택시를 타고 가라")
else:
    print("걸어가라")




print("\n======= in / not in =======")

#      in       /   not in
# x in 리스트       x not in 리스트
# x in 튜플         x not in 튜플
# x in 문자열       x not in 문자열


print(1 in [1, 2, 3])  # True
print(1 not in [1, 2, 3])  # False
print('a' in ('a', 'b', 'c'))  # True
print('j' not in 'python') # True


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print('걸어가라')




print("\n======= pass =======")

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    pass
else:
    print('걸어가라')

