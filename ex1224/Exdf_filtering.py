import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

titanic = sns.load_dataset('titanic')
print(titanic)
print()
print(titanic.head(10))
print()
titanic.info()
print()

df = titanic.loc[0:9, ['age', 'fare']]
print(df)
print()

print('\n-------- 데이터 필터링 --------\n')
print(df['age'])
print()

print('\n-------- 논리 연산자 --------\n')
print(df.loc[~(df['age'] < 20)])
print()

print('\n-------- and & --------\n')

print(titanic.loc[((titanic['age'] >= 10) & (titanic['age'] < 20))].head())
print()

mask1 =(titanic['age'] >= 10) & (titanic['age'] < 20)
print(mask1)
print()
print(type(mask1))
print()

df_teen = titanic[mask1]
print(df_teen.head())
print()

mask2 =(titanic['sex'] == 'female') & (titanic['age'] < 10)
df_teen_female = titanic[mask2]
print(df_teen_female.head())
print()

print('\n-------- or | --------\n')

mask3 = (titanic['age'] < 10) | (titanic['age'] > 60)
df_young_old = titanic.loc[mask3,['age','who']]
print(df_young_old.iloc[10:20])
print()

print(mask3)
print()

print('\n-------- -------- --------\n')

'''
탑승 도시가 Queenstown, Southampton 인 두곳만 필터링
'''
mask1 = titanic['embark_town'] == 'Queenstown'
mask = titanic['embark_town'] == 'Southampton'
df_boolean = titanic[mask1|mask2]
print(df_boolean.head())
print()
