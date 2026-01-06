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

df[['age_mean', 'survived_mean']] = grouped[['age', 'survived']].transform('mean')
print(df.head())
print()

def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped['age'].transform(z_score)
print(age_zscore.head())
print()

age_zscore2 = grouped['age'].transform(lambda x: (x - x.mean()) / x.std())
print(age_zscore2.head())
print()

age_zscore3 = (df['age'] - grouped['age'].transform('mean')) / grouped['age'].transform('std')
print(age_zscore3.head())
print()

# class 그룹별로 그룹바이 -> 그룹별 최대 나이와 최소 나이 컬럼 추가 -> 그룹별 최소나이 차이 컬럼 추가
df['age_min'] = grouped['age'].transform('min')

df['age_max'] = grouped['age'].transform('max')

df['age_diff_min'] = df['age'] - df['age_min']

print(df[['class', 'age', 'age_max', 'age_min', 'age_diff_min']].head())
print()