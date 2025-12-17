# 문자열(string)
# "Life is too short, You need Python"
# "a"
# "123"

print("\n======= 문자열 표현 방식 4가지 =======")

print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')



print("\n======= 문장 안에 따옴표 넣기 =======")

food = "Python's favorite food is perl"
print(food)

# 에러 food = 'Python's favorite food is perl'


say = '"Python is very easy." he says.'
print(say)

food = 'Python\'s favorite food is perl'
print(food)

say = "\"Python is very easy.\" he says."
print(say)


print("\n======= 변수사용 여러줄 작성 =======")

multiline='''
Life is too short
You need python
'''
print(multiline)

multiline="""
Life is too short
You need python
"""
print(multiline)


multiline = "Life is too short\nYou need python"
print(multiline)


print("\n======= 이스케이프 코드 =======")
# 자주 사용하는 코드 ----  \n  \'  \"  \t  \\ 

slamdunk = '''
강백호\t\t\\덩크\t\\33
통키\t\t\\불꽃슛\t\\100
세일러문\t\\변신\t\\7
'''

print(slamdunk)

