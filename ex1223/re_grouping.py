import re
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())
print()

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p.search('park 010-1234-5678')
print(m.group())
print()

# 원하는 부분만
p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-5678')
print(m.group()) # print(m.group(0))과 동일
print(m.group(1))
print(m.group(2))
print(m.group(3))
print()

text = '문의: hello.world@python.org'
pat = r'\w+[:]\s+(\w+\.\w+)[@](\w+\.\w+)'

m = re.search(pat, text)
print('전체: ',m.group())
print('사용자명: ', m.group(1))
print('도메인: ', m.group(2))
print()

# 문자열 재참조
p = re.compile(r'\b(\w+)\s+\1\b')
# 같은 단어가 공백을 사이에 두고 두번 연속 나오는 경우
m = p.findall('Paris in in the the spring')
print(m)
print()

text = '와아아 대박!!! 굿굿굿 ㅋㅋㅋㅋ'
pat = r'(.)\1{2,}'
m = re.search(pat, text)
print(m.group())
print()


result = re.sub(pat, r"\1", text)
print(result)
print()

text = """
문의: cs@test.co / backup: me.example+dev@sub-domain.example.com
스팸: a@b, user@.com, @nohost, 정상: hello.world@domain.io
"""

print("----- 전화번호 정규화(하이픈 통일) -----")
# 0으로시작
# 맨앞이 0포함 2~3자리
# 가운데가 3~4 자리
# 끝이 4 자리
text = "고객센터 02-123-1234, 01012341234, 031.123.1234, 010 1234 1234(대표)"

rx = re.compile(r"\b(0\d{1,2}?)[-. ]?(\d{3,4})[-. ]?(\d{4})\b")
# 000-0000-0000
normalized = rx.sub(r"\1-\2-\3", text)
print("정규화:", normalized)

m = rx.finditer(text)
print(m)

for i in m:
    print('원본:', i.group(0), "| 지역:", i.group(1), 
          "| 국번호:", i.group(2), "| 가입자:", i.group(3))