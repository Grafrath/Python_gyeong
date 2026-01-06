import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

print(df)
print()

# class로 그룹바이
grouped = df.groupby(['class'], observed=True)

# fare 열을 그룹별로 누적 합산
print(grouped['fare'].cumsum())
print()

print(grouped['fare'].sum())
print()

df['fare_cumsum'] = grouped['fare'].cumsum()
print(df.head())
print()

# 컬럼은 생성되지만 데이터는 NaN으로 채움
df['fare_sum'] = grouped['fare'].sum()
print(df.head())
print()

# transform
# 그룹단위로 계산을 수행하지만, 결과의 인덱스/행 수는 원본과 동일하게 반환


# transform에 누적함수 적용
print(grouped[['fare']].transform('cumsum'))
print()

# transform에 집계함수 적용
print(grouped[['age', 'survived']].transform('sum'))
print()

# 원본에 바로 붙여 보기
df[['age_mean', 'survived_mean']] = grouped[['age', 'survived']].transform('mean')
print(df.head())
print()

# z-score를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean()) / x.std()

# transform에 함수 적용
age_zscore = grouped['age'].transform(z_score)
print(age_zscore)
print()

# 위 내용을 람다로.
age_zscore2 = grouped['age'].transform(lambda x: (x - x.mean()) / x.std())
print(age_zscore2)
print()

# 위와 같은 동작
age_zscore3 = (df['age'] - grouped['age'].transform('mean')) / grouped['age'].transform('std')
print(age_zscore3)

# class 그룹별로 그룹바이 -> 그룹별 최대 나이와 최소 나이 컬럼을 추가 -> 또한 그룹별 최소 나이와이 차이 컬럼 추가.

df['max_age'] = grouped['age'].transform('max')
df['min_age'] = grouped['age'].transform('min')
df['min_diff'] = grouped['age'].transform(lambda x: (x - x.min()))
print(df.head())

print(grouped['age'].min())
