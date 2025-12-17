print('\n======= 문자열 포매팅1 =======')

print("I eat %d apples." % 5)

print("I eat %s apples." % "five")


number = 3
print("I eat %d apples" % number)



number = 10
day = "three"

print("I ate %d apples, so I was sick for %s days." % (number, day))


# 문자열 포맷 코드
# %d 정수
# %s 문자열  
# %c 문자열 1개  
# %f 소수  
# %o 8진수  
# %x 16진수  
# % 그 자체 >> %%

# %s 는 어떤 형태의 값이든 (문자열로) 변환해서 넣을 수 있다.

print("I have %s apples" % 3)
print("rate is %s" % 3.234)


print("오차는 2% 미만입니다.")

# 문자열 포매팅 안에서 % 표현하고 싶으면 %% 라고 써 줘야 한다.
print("오차는 %d%% 입니다" % 2)



# 제 이름은 OOO 이고 나이는 OOO 이고 전완근 둘레는 OOO 입니다.

print()
name = '홍길동'
age = 27
arm = 33.3

print("제 이름은 %s 이고, 나이는 %s살 이고, 전완근 둘레는 %scm 입니다." %(name, age, arm))

