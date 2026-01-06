import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

print(df.head())
print()

# class로 그룹바이
grouped = df.groupby(['class'], observed=True)


# 원본 통계정보
print(df.describe())
print()

# 각 그룹별로 'age', 'survived'  의  describe()
agg_grouped = grouped[['age', 'survived']].apply(lambda x: x.describe())
print(agg_grouped)
print()

# z-score 계산
def z_score(x):
    return (x - x.mean()) / x.std()

print('\n======= apply(z_score) =======\n')

age_zscore = grouped[['age', 'survived']].apply(z_score)
print(age_zscore)
print()

# transform에 함수 적용 (비교)
trans_zscore = grouped[['age', 'survived']].transform(z_score)
print(trans_zscore.head(50))


age_filter = grouped[['age']].apply(lambda x: x['age'].mean() < 30)
print(age_filter)

# age_filter 에서 값이 True인 인덱스 Second, Third 만 뽑기
# isin을 사용하여 원본(df)의 'class' 열에서 Second, Third 에 해당하는 행만 필터링
# 필터링 하면서, 컬럼은 'class', 'age', 'survived'만 loc

print()
print(df.loc[df['class'].isin(age_filter[age_filter].index), ['class', 'age', 'survived']])
print() # age_filter가 이미 bool 시리즈 이므로 age_filter==True 와 똑같음

# 아래와 같음
age_filter2 = grouped.filter(lambda x: x['age'].mean() < 30)
print(age_filter2[['class', 'age', 'survived']])