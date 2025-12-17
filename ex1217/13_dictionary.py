print('\n======= 딕셔너리 =======')
# "이름" = "홍길동"   
# "key" = "value"

a = {1 : 'hi'}
a = {'a' : [1, 2, 3]}


print("\n======== 딕셔너리 생성/추가 =========")

# a[키] = 값   추가/수정

a = {1 : 'a'}
print(a)  # {1: 'a'}

a[2] = 'b'
print(a)  # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)  # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1, 2, 3]
print(a)  # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

del a[1]
print(a) # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

c = {"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}



print("\n======== 딕셔너리 값(value) 조회 =========")

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])  # 10
print(grade['julliet'])  # 99

a = {1:'a', 2:'b'}
print(a[1])  # a
print(a[2])  # b

a = {'a':1, 'b':2}
print(a['a'])  # 1
print(a['b'])  # 2

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(dic['name'])  # pey
print(dic['phone']) # 010-9999-1234
print(dic['birth']) # 1118

print("\n======= 주의사항 =======")
print("======= 키값은 고유하다, 중복X =======")

a = {1:'a', 1:'b'}
print(a)  # {1: 'b'}
# 기존 값을 덮어 씀

print("\n======= 키값에 리스트X, 튜플O =======")
# a = {[1,2] : 'hi'}
# print(a) --- TypeError: unhashable type: 'list'
# 키 값은 변할 수 없어야 한다.

a = {(1,2) : 'hi'}
print(a)