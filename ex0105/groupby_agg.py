import pandas as pd
import seaborn as sns
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'], observed=True)
print(grouped)
print()

std_all = grouped.std(numeric_only=True)
print(std_all)
print()

std_all_index = df.groupby(['class'],
                           observed=True, as_index=False).std(numeric_only=True)
print(std_all_index)
print()

print('\n======== -------- ========\n')

print(grouped[['class', 'sex']].value_counts())
print()

print(df[['class', 'sex']].value_counts())
print()

print(df['class'].value_counts())
print()

print('\n======== agg메서드 ========\n')

agg_mean = grouped.aggregate('mean', numeric_only=True)
print(agg_mean)
print()

# agg로 쓸수있음
agg_mean2 = grouped.agg('mean', numeric_only=True)
print(agg_mean2)
print()

agg_max = grouped.agg('max')
print(agg_max)
print()

agg_min = grouped.agg('min')
print(agg_min)
print()

print('\n======== -------- ========\n')

agg_all = grouped[['age', 'fare', 'survived']].agg(['mean', 'max'])
print(agg_all)
print()

agg_sep = grouped.agg({
    'age': 'mean',                   # 나이는 평균만
    'fare': ['min', 'max'],          # 요금은 최소값, 최대값 둘 다
    'survived': 'mean'               # 생존율(평균)
})
print(agg_sep)
print()

