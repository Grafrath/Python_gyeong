import pandas as pd
import seaborn as sns

# 1번 문제에 예시로 적어드린 것 처럼 문제 번호 프린트 꼭 해주세요.

# 모든 인터넷창과 카카오톡 등 메신저를 꺼주세요.
# 아래 주석 밑에 코드 적으시면 됩니다. 
# 결과만 같으면 코드가 달라도 상관 없습니다.
# 수업시간에 안 배운 코드는 감점입니다.
# 오른쪽 괄호에 있는 숫자가 배점입니다.
# 부분점수 있습니다, 최선을 다하세요!
# 파일이름은 '홍길동_pandas.py' 로 부디 맞춰 주세요.
# 13:20 까지 디스코드 DM 으로 제출.
# 즐거운 평가 되세요 ^^

# 1. seaborn 에서 타이타닉 데이터를 로드하시오. (2)
print('\n------------ 1번 문제 ------------\n')
titanic = sns.load_dataset('titanic')

# 2. 타이타닉 데이터를 프로젝트 "루트 디렉토리"에 titanic.csv로 저장하시오. (2)
print('\n------------ 2번 문제 ------------\n')
titanic.to_csv('./titanic.csv', encoding='utf-8-sig')
print('csv 파일로 저장 완료')

# 3. 타이타닉 데이터의 첫 5개 행을 출력하시오. (2)
print('\n------------ 3번 문제 ------------\n')
print(titanic.head())

# 4. 터미널에 모든 컬럼이 한 라인에 보이도록 조치하시오. (2)
print('\n------------ 4번 문제 ------------\n')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 300)

# 5. 타이타닉 데이터의 "마지막" 70개 행을 (터미널에 생략없이 출력도록 조치하고) 출력하시오. (2)
print('\n------------ 5번 문제 ------------\n')
print(titanic.tail(70))

# 6. 타이타닉 데이터의 인포메이션을 출력하시오. (2)
print('\n------------ 6번 문제 ------------\n')
titanic.info()

# 7. 컬럼별 널값 개수를 보여주는 시리즈를 출력하시오. (3)
print('\n------------ 7번 문제 ------------\n')
print(titanic.isnull().sum())

# 8. 널값이 있는 컬럼만 뽑아 개수를 아래처럼 각각 출력하시오. (7)
'''
age 널값: 177개
embarked 널값: 2개
deck 널값: 688개
embark_town 널값: 2개
'''
print('\n------------ 8번 문제 ------------\n')
n_count = titanic.isnull().sum()
for col in n_count[n_count > 0].index:
    print(f"{col} 널값: {n_count[col]}개")

# 9. survived, pclass, sex, age, class, deck, fare, embarked 컬럼만 df 에 담고 헤드 출력. (2)
print('\n------------ 9번 문제 ------------\n')
df = titanic[['survived', 'pclass', 'sex', 'age', 'class', 'deck', 'fare', 'embarked']].copy()
print(df.head())

# 10. deck, pclass 컬럼은 드랍하고 헤드출력. (inplace=True 사용하시오) (2)
print('\n------------ 10번 문제 ------------\n')
df.drop(['deck', 'pclass'], axis=1, inplace=True)
print(df.head())

# 11. sex 컬럼 이름을 gender 로 바꾸고 헤드출력. (3)
print('\n------------ 11번 문제 ------------\n')
df.rename(columns={'sex': 'gender'}, inplace=True)
print(df.head())

# 12. 컬럼 순서를 class, age, gender, fare, survived, embarked 순서로 바꾸고 헤드출력. (3)
print('\n------------ 12번 문제 ------------\n')
df = df[['class', 'age', 'gender', 'fare', 'survived', 'embarked']]
print(df.head())



# 13. 인덱스 825~831번 데이터의 age, embarked만 조회하시오. (2)
print('\n------------ 13번 문제 ------------\n')
df_et = df[['age', 'embarked']][825:831]
print(df_et)


# 14. ebarked의 널값을 "이전행"과 같은 값으로 채우고 embarked 컬럼의 825~831 행을 조회. (3)
print('\n------------ 14번 문제 ------------\n')
df['embarked'] = df['embarked'].ffill()
print(df['embarked'][825:831])
print()


# 15. gender_ini 라는 컬럼을 추가해서 남성인 경우 m, 여성인 경우 f 로 채운 후 df 헤드출력. (4)
print('\n------------ 15번 문제 ------------\n')
df['gender_ini'] = df['gender'].apply(lambda x: 'm' if x == 'male' else 'f')
print(df.head())


# 16. 20살 이상의 남성만 필터링한 후, 나이와 성별만 상위 10개 행 출력. (3)
print('\n------------ 16번 문제 ------------\n')
mask = (df['age'] >= 20) & (df['gender'] == 'male')
print(df[mask][['age', 'gender']].head(10))


# 17. df의 산술정보를 조회하시오. (2)
print('\n------------ 17번 문제 ------------\n')
print(df.describe())
print()
print(df.describe(include='object'))
print()
print(df.count())
print()

uv = df['gender'].value_counts()
print(uv)
print()

# 18. 전체 age의 평균을 소수점 아래 두자리로 정리하여 출력하시오. (3)
print('\n------------ 18번 문제 ------------\n')
age = df['age'].mean().round(2)
print(f"{age:.2f}")

# 19. age의 널값을 age 평균으로 채운후 전체 info 조회. (3)
print('\n------------ 19번 문제 ------------\n')
df['age'] = df['age'].fillna(age)
df.info()

# 20. class 열의 고윳값을 조회하시오. (2)
print('\n------------ 20번 문제 ------------\n')
print(df['class'].unique())

# 21. class 열의 데이터 타입을 category로 변환후 info 조회. (2)
print('\n------------ 21번 문제 ------------\n')
df['class'] = df['class'].astype('category')
df.info()

# 22. 0~20살, 20~60살, 60~100살 구간으로 나누어, 
# 각각 child, adult, elder 로 할당한 컬럼 young_old 를 추가한 후 df 상위 30개 행 출력. (7)
print('\n------------ 22번 문제 ------------\n')
bins = [0, 20, 60, 100]
bin_name = ['child', 'adult', 'elder']
df['young_old'] = pd.cut(df['age'], bins=bins, labels=bin_name, include_lowest=True)
print(df.head(30))

# 23. age와 fare의 max, min 값을 출력하시오. (apply 사용) (4)
print('\n------------ 23번 문제 ------------\n')
print(df[['age', 'fare']].apply(lambda x: [x.max(), x.min()], axis=0))

# 24. 클래스와 성별로 그룹화 하여 "Third" 클래스의 "남성" 그룹만 헤드 조회. (3)
print('\n------------ 24번 문제 ------------\n')
grouped = df.groupby(['class', 'gender'], observed=False)
print(grouped.get_group(('Third', 'male')).head())

# 25. 위에서 그룹화한 데이터들의 평균을 조회하시오. (3)
print('\n------------ 25번 문제 ------------\n')
print(grouped.mean(numeric_only=True))

# 26. agg 를 사용하여 정확히 다음과 같이 출력하시오. (4)
'''
                    fare        age      
                     std       mean   max
class  gender
First  female  74.259988  34.141489  63.0
       male    77.548021  39.287869  80.0
Second female  10.891796  28.748684  57.0
       male    14.922235  30.653981  70.0
Third  female  11.690314  24.068750  63.0
       male    11.681696  27.372392  74.0
'''
print('\n------------ 26번 문제 ------------\n')
agg_df = grouped.agg({'fare': 'std', 'age': ['mean', 'max']})
print(agg_df)
# 27. class별 나이 평균을 적어 놓은 컬럼 cl_age_mean 추가 후 헤드 조회. (5)
'''
   class   age  gender     fare  survived embarked gender_ini youg_old  cl_age_mean
0  Third  22.0    male   7.2500         0        S          m    adult    26.403503
1  First  38.0  female  71.2833         1        C          f    adult    37.048241
2  Third  26.0  female   7.9250         1        S          f    adult    26.403503
3  First  35.0  female  53.1000         1        S          f    adult    37.048241
4  Third  35.0    male   8.0500         0        S          m    adult    26.403503
'''
print('\n------------ 27번 문제 ------------\n')
df['cl_age_mean'] = grouped['age'].transform('mean')
print(df.head())

# 28. 적절한 조치를 취하여 다음과 같이 출력하시오 (5)
'''
                     age                   fare             survived           cl_age_mean     
                    mean        std        mean        std      mean       std        mean  std
class  gender
First  female  34.141489  13.017989  106.125798  74.259988  0.968085  0.176716   37.048241  0.0
       male    39.287869  14.446400   67.226127  77.548021  0.368852  0.484484   37.048241  0.0
Second female  28.748684  12.700882   21.970121  10.891796  0.921053  0.271448   29.867011  0.0
       male    30.653981  14.161005   19.741782  14.922235  0.157407  0.365882   29.867011  0.0
'''
print('\n------------ 28번 문제 ------------\n')
result = grouped[['age', 'fare', 'survived', 'cl_age_mean']].agg(['mean', 'std'], numeric_only=True)
print(result)

# 29. 성별, 나이, 클래스만 남긴 df2를 새로 만들고 age가 널값인 행의 인덱스를 "리스트"로 출력 (5)
print('\n------------ 29번 문제 ------------\n')
df2 = titanic[['sex', 'age', 'class']].copy()
null_idx = df2[df2['age'].isnull()].index.tolist()
print(f"Age 널값 인덱스: {null_idx}")

# 30. 클래스 & 성별 별 나이 평균으로 age 널값을 채우고 상위 50행 출력. (8)
print('\n------------ 30번 문제 ------------\n')
print(df2.head(10))
cl_gen = df2.groupby(['class', 'sex'], observed=False)
df2['age'] = df2['age'].fillna(cl_gen['age'])
print(df2.head(50))


