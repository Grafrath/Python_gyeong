import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

print(df)
print()

# class로 그룹바이
grouped = df.groupby(['class'], observed=True)
print(grouped)

# 그룹별로 첫 2행을 확인
grouped_head = grouped.head(2)
print(grouped_head)
print()

# 각 그룹의 n번 인덱스 데이터를 확인
grouped_first = grouped.nth(200)
print(grouped_first)
print()

# 200번으로 조회 -> second 그룹은 안뜬다.
print(grouped[['class', 'age', 'survived']].nth(200))
print()

# 데이터 개수가 200개 이상인 그룹만을 필터링하여 반환
grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter)
print()

for key, group in grouped:
    print('key :', key)
    print('number :', len(group))
    print(group.head())
    print()

# age의 평균이 30보다 작은 그룹만을 필터링 하여 반환

print(grouped['age'].mean())
print()

age_filter = grouped.filter(lambda x: x['age'].mean() < 30)
print(age_filter.head(100))