import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)
print()

m = p.match("3 python")
print(m)
print()

m = p.search("python")
print(m)
print()

m = p.search("3 python")
print(m)
print()

result = p.findall("life is too short")
print(result)
print()

result = p.finditer("life is too short")
print(result)
print()

for r in result: print(r)
print()

'''
match 객체의 메서드 종류

group	매치된 문자열을 반환한다.
start	매치된 문자열의 시작 위치를 반환한다.
end	매치된 문자열의 끝 위치를 반환한다.
span	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환한다.
'''

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print()