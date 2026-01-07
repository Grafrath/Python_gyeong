import pandas as pd
import seaborn as sns
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
grouped = df.groupby(['class'], observed=True)

print(df.head(3))
print(grouped)
print()

print('\n-------- pivot-table --------\n')

pdf1 = pd.pivot_table(df, index='class', # class가 행
                      columns='sex', values='age', # sex가 열, age가 데이터
                      aggfunc='mean', observed=True) # 데이터 집계함수
print(pdf1)
print()

pdf2 = pd.pivot_table(df, index='class', # class가 행
                      columns='sex', values='survived', # sex가 열, age가 데이터
                      aggfunc=['mean', 'sum'], observed=True) # 데이터 집계함수
print(pdf2)
print()

pdf3 = pd.pivot_table(df, index='class', # class가 행
                      columns='sex', values='survived', # sex가 열, age가 데이터
                      aggfunc=['mean', 'sum'], observed=True) # 데이터 집계함수
print(pdf3)
print()

print('\n-------- stack --------\n')

df = pdf3
df_stacked = df.stack(future_stack=True)
print(df_stacked)
print()

df_unstacked = df_stacked.unstack()
print(df_unstacked)
print()

df_unstacked = df_stacked.unstack(level=0)
print(df_unstacked)
print()

df_unstacked2 = df_unstacked.unstack(level=1)
print(df_unstacked2)
print()


