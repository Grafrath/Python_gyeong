import seaborn as sns
import pandas as pd

# titanic 데이터셋 로드, age, fare 열만 뽑아서 df 만들기 해보세요.

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]

print(df.head())
print()

# 숫자를 넣으면 10이 더해져서 나오는 함수 add_10 정의
def add_10(n):
    return n + 10

# 숫자 두개를 넣으면 합한 값이 나오는 함수 add_two_obj 정의
def add_two_obj(a, b):
    return a + b

print(add_10(10))
print(add_two_obj(10, 10))

print('\n======= apply(일반함수) =======\n')

# 시리즈에 apply
sr1 = df['age'].apply(add_10)
print(sr1.head())
print()

# 시리즈에 map
sr1 = df['age'].map(add_10)
print(sr1.head())
print()

# apply는 시리즈 통째로 접근
# map은 원소 하나하나에 접근

print('\n======= apply(람다함수) =======\n')

sr2 = df['age'].apply(lambda n: n + 10)
print(sr2.head())
print()

# 나머지 인수는 10으로..
sr3 = df['age'].apply(add_two_obj, b=10)
print(sr3.head())
print()

# 위 내용을 람다 함수로!
sr4 = df['age'].apply(lambda a, b: a + b, b=10)
print(sr4.head())
print()

# df['age']= df['age'] + 10  간단하게 할 수도 있다.
# 하지만 아래 같은 작업은 apply 혹은 map 사용

print('\n======= 복잡한 함수의 경우 =======\n')

def categorize_age(age):
    if age < 13:
        return 'child'
    elif age < 20:
        return 'teen'
    else:
        return 'adult'
    
df['age_group'] = df['age'].apply(categorize_age)
print(df['age_group'])
print()

df['age_group'] = df['age'].map(categorize_age)
print(df['age_group'])


print('\n======= 시리즈의 원소에 map()적용 =======\n')

def over_thirty(age):
    return age > 30

sr_map = df['age'].map(over_thirty)
print(sr_map.head())
print()

# 위 내용을 람다 함수로!
sr_map2 = df['age'].map(lambda age: age > 30 )
print(sr_map2.head())



print('\n======= map()에 딕셔너리 적용 =======\n')

print(titanic)
print()
print(titanic['sex'].unique())
print()

gender_dict = {'male':0, 'female':1}
titanic['gender'] = titanic['sex'].map(gender_dict)
titanic.info()
print()
print(titanic)
print()