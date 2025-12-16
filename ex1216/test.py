#유니코드 기본지원입니다.

'''
기본적으로 UTF-8 인코딩 방식을 따르는 유니코드 문자열입니다.
따라서 영문, 한글, 이모지 등을 별도 처리 없이 자연스럽게 섞어 쓸 수 있습니다.
'''

print('\n============ 유니코드 ============')
print()

# 유니코드는 2Byte=0부터 65,535, 아스키는 1Byte=0부터 255
kor = "안녕하세요" #C언어처럼 아스키코드가 기본값일경우 해당 배열의 크기는 11이다.
eng = "abcde"

for ch in kor:
    print(ch, ord(ch))

for ch in eng:
    print(ch, ord(ch))

print()

print(len(kor))
print(len(eng))

#별도의 문자타입이 없습니다.
#파이썬은 언어레벨에서 동적할당을 지원합니다.

print('\n============ 문자타입 ============')
print()

a = 'a'
print(a)
print(a[0])

'''
c 얘기를 잠깐 해야됩니다.
int num = 97
char ch = 'a'
ch의 값은 a 라고 생각되지만 ch의 값은 97
97이란 값을 문자로 어떻게 보여주는지 정한 약속이 아스키코드와, 유니코드
즉 "abc"란 문자열은 {97, 98, 99} 란 값을 가진 배열입니다.

처음에는 char형이 있고 문자열은 char에 배열선언해서 사용했습니다.
char str[] = "hello"
이걸 귀찮다, 자동으로 선언 하자고 나온게 String 
더 발전해서 그냥 애초에 배열로 받자 식으로 진행되었습니다.
'''

'''
C / Java: 'a'는 문자(char), "abc"는 문자열(string)로 엄격히 구분됩니다.
Python: 문자 하나도 길이가 1인 문자열로 취급합니다.
문자 타입이 없다보니 '' 와 "" 를 구분하지 않습니다.
그래서 ''' ''', """ """를 모두 사용 가능합니다.
'''

# ''', """은 여러 줄 문자열(Multi-line String)
print('\n============ 여러줄 문자열 ============')
print()
# 1. 큰따옴표 3개 (Triple Double Quotes)를 사용한 예제
# 주로 일반적인 텍스트나 Docstring을 작성할 때 사용합니다.
long_text = """
안녕하세요!
이것은 파이썬의 여러 줄 문자열 예제입니다.

줄 바꿈 문자(\n)를 사용하지 않고도
작성한 그대로의 형식을 유지할 수 있습니다.
"""

print("--- 예제 1: 일반 텍스트 ---")
print(long_text)


# 2. 작은따옴표 3개 (Triple Single Quotes)를 사용한 예제
# 문자열 내부에 큰따옴표(")가 포함되어야 할 때 유용합니다.
code_snippet = '''
def greet(name):
    # 이 함수는 인사를 출력합니다.
    print(f"Hello, {name}!")

greet("Gemini")
'''

print("\n--- 예제 2: 코드/문서 내 인용부호 ---")
print(code_snippet)

#직관적인 연산자

print('\n============ 연산자 ============')
print()

head = "Python"
tail = " is fun!"
print(head)
print(tail)
print()

print(head + tail)
print()

text = head*3
print(text)
print()

#-인덱싱, 슬라이싱

print('\n============ 인덱싱 ============')
print()
# 인덱스값을 사용하여 문자열에서 특정 위치의 문자를 추출하기!
ex = "ABCDE"
print(ex[2])                        # C       출력!

# 여러 문자를 추출하기!
print(ex[0],ex[1],ex[2])            # A B C   출력!
print(ex[0],ex[1],ex[2], sep="")    # ABC     출력!
# print(ex[0,1,2]) 사용불가.




# 마이너스 인덱스 문자 추출하기!
# 문자열의 뒤에서부터 번호를 부여하는 방식
# 뒤에서 첫번째 문자는 -1로 시작한다!

ex = "ABCDE"
print(ex[-2])                       # D       출력!
print(ex[-1],ex[-2],ex[-3])         # E D C   출력!
print(ex[-1],ex[-2],ex[-3], sep="") # EDC     출력!

print('\n============ 슬라이싱 ============')
print()

text = "LoL Top Liner"

substring1 = text[0:3]      # 기본값 입력
print(substring1)           # LoL 출력

substring2 = text[:3]       #시작 기본값 0 생략
print(substring2)           # LoL 출력


substring3 = text[4:13]      # 기본값 입력
print(substring3)           # Top Liner 출력

substring4 = text[4:]       #종료 기본값 생략
print(substring4)           # Top Liner 출력


print(text[:])              # 시작 종료 기본값 생략
                            # LoL Top Liner 출력

# Liner 문자열을 전부 출력하는것이 아니라 인덱스 8부터 인덱스12까지 2씩 증가하는 인덱스만 출력
substring5 = text[8:13:2]   # 8, 10, 12
print(substring5)           # Lnr 출력

print('\n============ 문자열 메서드 ============')
print()

#-문자열에서 자주 쓰이는 메서드
s = "abcd"
s.count("a") # a의 갯수
print(s.count("a"))
s_upper = s.upper()
s_replace = s_upper.replace("A","e")
print(s, s_upper, s_replace) # abcd ABCD eBCD
parts = s.split("b")
print(parts) # ['a', 'cd']

'''
아래는 몇 가지 이스케이프 코드입니다.

\n	문자열 안에서 줄을 바꿀 때 사용
\t	문자열 사이에 탭 간격을 줄 때 사용
\\	\를 그대로 표현할 때 사용
\'	작은따옴표(')를 그대로 표현할 때 사용
\"	큰따옴표(")를 그대로 표현할 때 사용
\r	캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
\f	폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
\a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b	백 스페이스
\000	널 문자
'''

print('\n============ 이스케이프 ============')
print()
text = "P       ython"
print(text)
text = "P\tython"
print(text)

text = "P 'ython'"
print(text)
text = 'P \'ython\''
print(text)

text = '"P" ython'
print(text)
text = "\"P\" ython"
print(text)

# 인터닝 기법을 사용한다
# 파이썬의 문자열은 불변성을 가집니다.

print('\n============ 불변성 ============')
print()

a = "Pithon"
print(a+"?")
print(a[1]+"...")
# Pithon을 Python으로 바꾸고싶은데...
# a[1] = 'y' TypeError

print(a[:1] + 'y' + a[2:]) # Python

print('\n============ 인터닝 ============')
print()

ex1 = 'String'
ex2 = "String"
ex3 = 'Str'
ex4 = 'ing'
ex5 = 'Str' + 'ing'
ex6 = ex3 + ex4

print('\n============ 내용비교 ============')
print()
# 문자열의 내용이 같은지 비교
print(ex1==ex2) #True
print(ex1==ex5)
print(ex1==ex6)

print('\n============ 주소비교 ============')
print()
# 주소가 같은지 비교
print(ex1 is ex2) #True
print(ex1 is ex5) #True
print(ex1 is ex6) #False

#-예제-##############################################
# 다음을 출력하시오
'''
this is really 
long String
so i need line
'''
# 다음을 출력하시오
# he says "I like Python


test1 = "Python"
# 문자열에서 첫글자와 마지막 글자를 출력하시오(인덱싱만 사용)
# 문자열에서 뒤에서 4글자를 출력하시오

test2 = "0123456789"
# 다음 문자열에서 짝수 인덱스 문자만 출력하시오
# 다음 문자열을 거꾸로 출력하시오.
# 슬라이싱으로 87654 를 출력하시오
# 다음 문자열에서 홀수인덱스만 추출한다음 거꾸로 출력하시오 97531

test3 = "snfklsafnlwenffsdmfl;sdmfdiowfnewinbbsdfsefew"
# 다음 문자열의 절반 앞부분을 출력하시오
# 다음 문자열에서 가운데 3글자를 출력하시오 (test3 의 길이는 홀수이다.)


# 함수만들기
# 다음은 파이썬의 함수 문법을 위한 예시이다.
def add(a,c):
    kk = a+c
    return kk

# 문자열 s 가 주어질때 뒤집었을때도 같은지 여부를 반환하는 함수 isReverse 를 만드시오
# ex) s = "abcba" 일때  isReverse(s) 를 하면 True를 반환한다.

# 문자열 s가 주어질때 k 번째 문자를 제거한 문자열을 반환하는 함수 del_str 를 만드시오
# ex) s = "123456" , k = 3 일때
# del_str(s,k)을 하면 12356 을 반환한다.


# 문자열 p와 c가 주어질때 p가 c를 포함하는 횟수를 구하는 함수 count_c 를 만드시오
# ex) p = "abcdabba" , c = "ab" 일때
# count_c(p,c) 를 하면 2를 반환한다.


# 연속으로 같은 문자가 등장하면 압축하는 함수 zip_str을 만드시오.
# s = "aaabbbcca" 일때 압축하면 abca 이다
# s = "aaabbabcca" 일때 압축하면 ababca 이다

# ===============================================================