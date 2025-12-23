import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)
print()
# <re.Match object; span=(0, 6), match='python'>

m = p.match("3 python")
print(m)
print()
# None

m = p.search("python")
print(m)
print()

m = p.search("3 python")
print(m)
print()

'''
match 메서드는 문자열의 처음부터 정규식과 매치되는지 조사한다
"3 python" 문자열의 첫 번째 문자는 "3"이지만,
search는 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색하기 때문에
"3" 이후의 "python" 문자열과 매치된다.
'''

result = p.findall("life is too short")
print(result)
print()

# findall은 패턴과 매치되는 모든 값을 찾아 리스트로 반환한다.

result = p.finditer("life is too short")
print(result)
print()

for r in result: print(r)
print()

# finditer는 findall과 동일하지만
# 그 결과로 반복 가능한 객체(iterator object)를 반환한다.
# 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.

'''
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