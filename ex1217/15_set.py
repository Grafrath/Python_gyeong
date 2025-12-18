
print('\n======= 집합 =======')

s1 = set([1, 2, 3])
print(s1) # {1, 2, 3}

s2 = set("Hello")
print(s2)  # {'e', 'o', 'H', 'l'}

s3 = {1, 2, 3}
print(s3) # {1, 2, 3}

s4 = {'a', 'b', 'c'}
print(s4)

s = set()
s = {}  # 이건 딕셔너리이므로 주의!

# 집합은 중복을 허용하지 않는다.
# 집합은 순서가 없다 (Unordered)
# 순서가 없기때문에 ==>> 인덱싱이 안된다!




print("\n======= 리스트/튜플로 변환 =======")

s1 = set([1, 2, 3])


l1 = list(s1)
print(l1)  # [1, 2, 3]
print(l1[0]) # 1


print()
t1 = tuple(s1)
print(t1)  # (1, 2, 3)
print(t1[0]) # 1




print("\n======= 교집합/합집합/차집합 =======")

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)  # 교집합 {4, 5, 6}
print(s1.intersection(s2))


print(s1 | s2 ) # 합집합 {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))


print(s1 - s2) # 차집합 {1, 2, 3}
print(s1.difference(s2))





print("\n======= 집합 관련 함수 =======")

s1 = set([1, 2, 3])
s1.add(4)
print(s1) # {1, 2, 3, 4}


s1.update([4, 5, 6, 7])
print(s1)  # {1, 2, 3, 4, 5, 6, 7}


s1.remove(4)
print(s1)
# s1.remove(99) --- 없는 값 제거 시도시 오류 --- KeyError: 99

s1.discard(99)  # 없는 값 제거 시도시 오류 안뜸
s1.discard(1)  # 있는 값 제거 수행.
print(s1)

s1.clear()
print(s1)
