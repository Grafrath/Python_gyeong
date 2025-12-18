print('\n===== 변수 variable =====')
# 변수_이름 = 변수에_저장할_값



a = 1
b = 'python'
c = [1, 2, 3]



# 변수 이름 짓기
# 1. 영문자, 숫자, 언더스코어(_)만 사용
# 2. 숫자로 시작할 수 없다.
# 3. 예약어는 사용할 수 없다.
# 4. 대소문자를 구분한다.



# 올바른 면수명 예시
name = '홍길동'
age = 25
user_name = 'gildong'
userName = 'gildong'
_private = "비공개"
count1 = 10


# ==================================================


'''
_name  
언더바로 시작하면 비공개로 사용하고 싶다는 관례
기능적인 제한을 주지는 않는다.



_
언더바 하나만 쓰는 경우 (임시변수, 무시해도 될때)
x, _, z = (1, 2, 3)  # 2는 사용하지 않음
'''




# ==================================================



# 잘못된 예시
# 1name = "홍길동"
# user-name = '홍길동'
# if = 10 

# 파이썬 예약어
# False, True, None, and, as, assert, break, class, continue, def,
# del, elif, except, finally, for, from, global, if, import, in
# is, lambda, nonlocal, not, or, pass, return, try, while......

# 의미가 명확한 이름을 사용한다.
# 너무 짧거나 긴 이름은 피한다.



# 좋은 예
student_name = '김철수'
total_score = 95
user_age = 20



# 안좋은 예
a = '김철수'
studentNameFromKorea = '김철수'



# 변수란???

a = [1, 2, 3]

# [1, 2, 3] 값을 가지는 리스트 데이터가 자동으로 메모리에 생성
# 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게 된다.

print(id(a))  # 2275536605504



b = a

print(id(a)) 
print(id(b)) # 같은 주소 값을 참조한다.
print(a is b) # a와 b가 가리키는 객체가 같을까?  True



a[1] = 4
print(a)
print(b)




print("\n======= 복사하기 =======")

a = [1, 2, 3]
b = a[:]

print(a)
print(b)

print(id(a)) 
print(id(b)) # (다른 주소를 참조)

a[1] = 4
print(a)
print(b)
print(a is b)
print()


a = [1, 2, 3]
b = a.copy()
print(b is a)




print("\n======= 변수를 만드는 여러가지 방법 =======")

a, b = ('python', 'life')
c, d = 'java', 'good'

print(a)
print(b)
print(c)
print(d)
print()



[e, f] = ['html', 'easy']
print(e)
print(f)
print()


g = h = 'python'
print(g)
print(h)
print()


a = 3
b = 5
a, b = b, a

print(a)
print(b)