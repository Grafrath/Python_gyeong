
print('\n======= 딕셔너리 관련함수 =======')

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}



print("\n======= 키값 조회 =======")

print(a.keys())  # dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)

b = list(a.keys()) # 리스트로 변환
print(b)




print("\n======= 밸류값 조회 =======")

print(a.values()) # dict_values(['pey', '010-9999-1234', '1118'])

c = list(a.values())
print(c) # ['pey', '010-9999-1234', '1118']




print("\n======= 키,밸류 조회 =======")
print(a.items())

d = list(a.items())
print(d)



print("\n======= 키,밸류 지우기 =======")
print(a)

a.clear()
print(a)




print("\n======= get =======")

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a['name'])
print(a.get('name'))
print(a.get('phone'))


# print(a['hobby'])     # 해당 키값 없으면 오류 --- KeyError: 'hobby'
print(a.get('hobby'))   # 키값 없으면 None 반환
print(a.get('hobby', '정보없음'))





print("\n======= in =======")

print('name' in a)
print('hobby' in a)


# 'name' in a.keys()
# 'pey' in a.values()





print("\n======= pop =======")

name = a.pop('name')
print(name)
print(a)

email = a.pop('email', '정보없음')
print(email)

