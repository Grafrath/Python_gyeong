print('\n======= 문자열 관련 내장함수 =======')

a = "hobby"
print(a.count('b'))
print()


a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))  # 찾는 값 없을 때는 -1 반환
print()


a = "Python is the best choice"
print(a.index('b'))
# print(a.index('k')) 찾는 값 없을 때는 에러 
print()


a = 'abcd'
print(",".join(a))  #a,b,c,d
print()


b = ['a', 'b', 'c', 'd']
print(".".join(b))  #a.b.c.d
print()


a = "hi"
print(a.upper())
print()

a = "HI"
print(a.lower())
print()



print("\n======= 스트립 =======")


a = "  hi  "
print(a)
print(a.lstrip())  # 왼쪽 공백 제거
print(a.rstrip())  # 오른쪽 공백 제거
print(a.strip())   # 양쪽 공백 제거


print()
print()


a = "Life is too short"
b = a.replace("Life", "Movie")
print(b)
print()


a = "Life is too short"
b = a.split()  # 공백(들)을 기준으로 분리
print(b)
print()


a = "Life:is:too:short"
b = a.split(':')
print(b)
print()


print("\n=== 문자열이 문자로만 이루어졌는지 확인 ===")

s = "Python"
print(s.isalpha()) # 알파벳만 있기 때문에 True

s = "파이썬"
print(s.isalpha()) # 문자라면 True

s = "Python3"
print(s.isalpha())  # 숫자가 있어서 False

s = "Hello world"
print(s.isalpha())  # 공백이 있어서 False



print("\n=== 문자열이 숫자로만 이루어졌는지 확인 ===")

s = "12345"
print(s.isdigit())

s = "1234a"
print(s.isdigit())

s = "12 45"
print(s.isdigit())



print("\n=== 문자열이 특정 문자(열)로 시작/끝 하는지 확인 ===")

s = "Life is too short"
print(s.startswith("Life"))
print(s.startswith("too"))
print()

print(s.endswith("short"))
print(s.endswith("is"))



# ==========================================
print()

logs = [
    "ERROR: 파일을 찾을 수 없습니다.",
    "INFO: 사용자가 로그인했습니다.",
    "ERROR: 데이터베이스 연결 실패",
]

error_count = sum(log.count("ERROR") for log in logs)
print(f"총 에러 로그 개수: {error_count}")


# ==========================================
print()

username = "홍길동"
if username.isalpha():
    print("사용자 이름이 올바릅니다.")
else:
    print("사용자 이름에는 숫자나 특수문자가 포함될 수 없습니다.")


# ==========================================
print()

filename = "   report_2025.txt   "
filename_clean = filename.strip()  # 양쪽 공백 제거
print(f"파일 이름: '{filename_clean}'")


# ==========================================
print()

data = "홍길동,20,서울"
name, age, city = data.split(",")
print(name, age, city)


# ==========================================
print()

filename = "report_2025.txt"
if filename.endswith(".txt"):
    print("텍스트 파일입니다.")





# ===========================================


#1 문자열 "banana"에서 문자 'a'의 개수를 출력하는 코드를 작성하시오.
print("banana".count("a"))
#2 문자열 "I like python"에서 문자 'p'가 처음 등장하는 위치를 출력하는 코드를 작성하시오.
# (※ find 사용)
print("I like python".find('p'))
#3 문자열 "Python is fun"에서 문자 'z'를 찾았을 때 에러 없이 결과를 출력하는 코드를 작성하시오.
print("Python is fun".find('z'))
#4 문자열 "study"의 각 문자를 -로 연결하여 출력하는 코드를 작성하시오.
# (예: s-t-u-d-y)
print("-".join("study"))
#5 리스트 ['2025', '12', '25']의 요소들을 /로 연결하여 날짜 형태로 출력하는 코드를 작성하시오.
print("/".join(['2025', '12', '25']))
#6 문자열 "Python"을 모두 대문자로 출력하는 코드를 작성하시오.
print("Python".upper())
#7 문자열 "HELLO"를 모두 소문자로 출력하는 코드를 작성하시오.
print("HELLO".lower())
#8 문자열 " hi "에서 양쪽 공백을 제거하여 출력하는 코드를 작성하시오.
print(" hi ".strip())
#9 문자열 " hello"에서 왼쪽 공백만 제거하여 출력하는 코드를 작성하시오.
print(" hello".lstrip())
#10 문자열 "Life is too short"에서 "Life"를 "Movie"로 바꿔 출력하는 코드를 작성하시오.
print("Life is too short".replace("Life","Movie"))
#11 문자열 "apple apple apple"에서 "apple"을 "banana"로 모두 바꿔 출력하는 코드를 작성하시오.
print("apple apple apple".replace("apple","banana"))
#12 문자열 "Life is too short"를 공백 기준으로 나누어 리스트로 출력하는 코드를 작성하시오.
print("Life is too short".split())
#13 문자열 "Life:is:too:short"를 : 기준으로 나누어 리스트로 출력하는 코드를 작성하시오.
print("Life:is:too:short".split(':'))
#14 문자열 "Python"이 문자로만 이루어졌는지 확인하여 결과를 출력하는 코드를 작성하시오.
print("Python".isascii())
#15 문자열 "Python3"이 문자로만 이루어졌는지 확인하여 결과를 출력하는 코드를 작성하시오.
print("Python".isalnum())
#16 문자열 "12345"가 숫자로만 이루어졌는지 확인하여 결과를 출력하는 코드를 작성하시오.
print("12345".isdecimal())
#17 문자열 "Life is too short"가 "Life"로 시작하는지 확인하여 결과를 출력하는 코드를 작성하시오.
print("Life is too short".startswith("Life"))
#18 문자열 "Life is too short"가 "short"로 끝나는지 확인하여 결과를 출력하는 코드를 작성하시오.
print("Life is too short".endswith("short"))
#19 문자열 " hello python "에서
# 양쪽 공백을 제거한 뒤 모두 대문자로 변환하여 출력하는 코드를 작성하시오.
print(" hello python ".upper().strip())
#20 문자열 "2025-12-25"를 - 기준으로 분리하여
# ['2025', '12', '25'] 형태의 리스트로 출력하는 코드를 작성하시오.
print("2025-12-25".split('-'))


'''
# 1
print("banana".count('a'))

# 2
print("I like python".find('p'))

# 3
print("Python is fun".find('z'))

# 4
print("-".join("study"))

# 5
print("/".join(['2025', '12', '25']))

# 6
print("Python".upper())

# 7
print("HELLO".lower())

# 8
print("   hi   ".strip())

# 9
print("   hello".lstrip())

# 10
print("Life is too short".replace("Life", "Movie"))

# 11
print("apple apple apple".replace("apple", "banana"))

# 12
print("Life is too short".split())

# 13
print("Life:is:too:short".split(':'))

# 14
print("Python".isalpha())

# 15
print("Python3".isalpha())

# 16
print("12345".isdigit())

# 17
print("Life is too short".startswith("Life"))

# 18
print("Life is too short".endswith("short"))

# 19
print("   hello python   ".strip().upper())

# 20
print("2025-12-25".split('-'))

'''