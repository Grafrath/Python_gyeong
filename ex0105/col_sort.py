import seaborn as sns

titanic = sns.load_dataset('titanic')
# df = titanic[['survived', 'pclass', 'sex', 'age']]
# df.info()
# print()

df = titanic.loc[:, 'survived':'age']
df.info()
print()

print('\n-------- 컬럼 정렬 --------\n')

columns = df.columns.to_list()

columns_sorted = sorted(columns)
df_sort = df[columns_sorted]
df_sort.info()
print()

columns_reverse = columns_sorted[::-1]
df_rev = df[columns_reverse]
df_rev.info()
print()

print('\n-------- 컬럼 선택 --------\n')

df1 = df[['pclass', 'sex', 'age']]
print(df1.head(3))
print()

df2 = df.reindex(columns=['pclass', 'sex', 'age'])
print(df2.head(3))
print()

df_renamed = df.rename(columns={'pclass': 'room_class', 'sex': 'gender'})
print(df_renamed.head(3))