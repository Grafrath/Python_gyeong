print('\n======= 리스트 자료형 =======')

odd = [1, 3, 5, 7, 9]
a = []
b = ['life', 'is', 'too', 'short']
c = [1, 2, 'life', 'is']
d = [1, 2, ['life', 'is']]




print('\n======= 리스트 인덱싱 =======')
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])  # 1 + 3 = 4
print(a[-1])  # 3




print('\n======= 리스트 안의 리스트 =======')
a = [1, 2, 3, ['a', 'b', 'c']]

print(a[0])  # 1
print(a[3])  # ['a', 'b', 'c']
print(a[-1]) # ['a', 'b', 'c']
print()


print(a[3][1])  # b
print(a[-1][-1]) # c




print('\n======= 삼중 리스트 =======')

a = [1, 2, ['a', 'b', ['Life', 'is']]]

# Life 를 뽑아 내시오.

print(a[-1][-1][0])




print('\n======= 리스트 슬라이싱 =======')

a = [1, 2, 3, 4, 5]
print(a[0:2])


print(a[:2])
print(a[2:])
print()



a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(a[2:5]) # [3, ['a', 'b', 'c'], 4]

print(a[3][:2])
# ['a', 'b']



