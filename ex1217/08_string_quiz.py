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