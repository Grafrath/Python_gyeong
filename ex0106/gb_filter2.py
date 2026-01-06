import pandas as pd
import seaborn as sns
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'], observed=True)

agg_grouped = grouped[['age', 'survived']].apply(lambda x: x.describe())
print(agg_grouped)
print()

def z_score(x):
    return (x - x.mean()) / x.std()

print('\n-------- apply(z_score) --------\n')

age_zscore = grouped[['age', 'survived']].apply(z_score)
print(age_zscore)
print()

trans_zscore = grouped[['age', 'survived']].transform(z_score)
print(trans_zscore)
print()

grouped_age = grouped[['age']].apply(lambda x: x['age'].mean() < 30)
print(grouped_age)
print()

age_filter = grouped['age'].apply(lambda x: x.mean() < 30)
print(age_filter)
print()

'''
age_filter 에서 값이 true 인 인덱스 second, third만 뽑기
isin 을 사용하여 원본(df)의 class열에서 second, third에 해당하는 행만 필터링
필터링 하면서, 컬럼은 'class', 'age', 'survived'만 loc
'''

print('\n-------- 여러가지 필터링 --------\n')

true_class = age_filter[age_filter == True].index
print(true_class)
print()

filtered_df = df.loc[df['class'].isin(true_class), ['class', 'age', 'survived']]
print(filtered_df)
print()