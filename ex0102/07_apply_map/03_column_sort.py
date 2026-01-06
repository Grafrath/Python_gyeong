import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.head())

df = titanic.loc[:, 'survived':'age']
df = titanic[['survived', 'pclass', 'sex', 'age']]

print(df.head())
print()



print('\n======= 열 이름의 리스트 만들기 =======\n')

print(df.columns)
print(df.columns.to_list())
print(list(df.columns))
print(df.columns.values) # 넘피 배열
columns = list(df.columns.values)
print(columns)


print('\n======= 알파벳 순/역순 으로 정렬하기 =======\n')

columns_sorted = sorted(columns, reverse=False)
print(columns_sorted)
print()

df_sorted = df[columns_sorted]  # df[['age', 'pclass', 'sex', 'survived']] 와 같음.
print(df_sorted.head(3))
print()

columns_reversed = sorted(columns, reverse=True)
print(columns_reversed)
print()

df_reversed = df[columns_reversed]
print(df_reversed.head(3))
print()



print('\n======= 컬럼 선택하기 =======\n')

df1 = df[['pclass', 'age', 'survived']]
print(df1.head(3))
print()

# 선택 오타 or 새로운 컬럼 >>>>>>>> 에러
# df2 = df[['pclass', 'ageeee', 'survived']]
# print(df2.head(3))

# reindex
df3 = df.reindex(columns=['pclass', 'age', 'survived'])
print(df3.head(3))
print()

# reindex 사용시 오타 or 새로운 컬럼 >>>>>>>>> (새로운 컬럼 만들어서 NaN으로 채움)
df3 = df.reindex(columns=['pclass', 'ageeee', 'survived'])
print(df3.head(3))
print()