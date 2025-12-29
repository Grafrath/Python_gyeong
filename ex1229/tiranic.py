'''
타이타닉 로드하기 (시본)
데이터 구조 확인
80세 노인분의 생존 여부
승객의 평균나이, 평균요금
age의 결측치를 age의 평균으로 채우기
deck 컬럼 제거
age, parch, class 열만 선택하여 보기
age, parch, class 열만 선택하여 랜덤 추출
FamiliySize 라는 컬럼에 sibsp + parch + 1(자기자신)
(로 해서 총 가족 인원수 컬럼 만들어보기)
IsChild 라는 True/False 컬럼 만들어보기 ( 13살 미만 )
불타입의 시리즈를 데이터[] 에 넣으면 True에 해당하는 데이터만 필터링
남성과 여성의 평균 나이 비교
id 라는 이름으로 정수 인덱스 주기
'''

import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

# 타이타닉 로드하기 (시본)
# 데이터 구조 확인
titanic = sns.load_dataset('titanic')
print(titanic.head(5))
print()
titanic.info()
print()

# 80세 노인분의 생존 여부
old_man = titanic[titanic['age'] == 80]
print(old_man[['age', 'alive', 'survived']])
print()

# 승객의 평균나이, 평균요금
age = titanic['age'].mean()
fare = titanic['fare'].mean()
print(f"평균나이: {age:.2f}, 평균요금: {fare:.2f}")
print()

# age의 결측치를 age의 평균으로 채우기
titanic['age'] = titanic['age'].fillna(age)
print(titanic['age'])
print()

# deck 컬럼 제거
titanic.drop('deck', axis=1, inplace=True)
print(titanic.head(5))
print()

# age, parch, class 열만 선택하여 보기
print(titanic[['age', 'parch', 'class']].head())
print()

# age, parch, class 열만 선택하여 랜덤 추출
print(titanic[['age', 'parch', 'class']].sample(5))
print()

# FamiliySize 라는 컬럼에 sibsp + parch + 1(자기자신)
# (로 해서 총 가족 인원수 컬럼 만들어보기)
titanic['FamilySize'] = titanic['sibsp'] + titanic['parch'] + 1
print(titanic['FamilySize'])
print()

# IsChild 라는 True/False 컬럼 만들어보기 ( 13살 미만 )
titanic['IsChild'] = titanic['age'] < 13
print(titanic['IsChild'])
print()

# 불타입의 시리즈를 데이터[] 에 넣으면 True에 해당하는 데이터만 필터링
titanic_child = titanic[titanic['IsChild']]
print(titanic_child.head())
print()

# 남성과 여성의 평균 나이 비교
print(titanic.groupby('sex')['age'].mean())
print()+

# id 라는 이름으로 정수 인덱스 주기
titanic.reset_index(inplace=True)
titanic.rename(columns={'index': 'id'}, inplace=True)
print(titanic[['id', 'sex', 'age', 'FamilySize']].head())
print()