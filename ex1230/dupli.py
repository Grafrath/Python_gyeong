import pandas as pd

df = pd.DataFrame({'c1':['a', 'a', 'b', 'b', 'b'],
                   'c2': [1, 1, 1, 2, 2],
                   'c3': [1,1,2,2,2]})

print(df)

print('\n-------- 중복값 --------\n')

df_duf = df.duplicated()
print(df_duf)
print()

df_duf = df.duplicated(keep='last')
print(df_duf)
print()

print('\n-------- 특정 컬럼 중복값 --------\n')

col_duf = df['c2'].duplicated()
print(col_duf)
print()

col_duf2 = df.duplicated(subset=['c2'])
print(col_duf2)
print()

col_duf3 = df.duplicated(subset=['c2', 'c3'])
print(col_duf3)
print()

print('\n-------- 중복값 제거 --------\n')

df_duf = df.drop_duplicates()
print(df_duf)
print()

df_duf = df.drop_duplicates(keep=False)
print(df_duf)
print()

df_duf = df.drop_duplicates(subset=['c2', 'c3'])
print(df_duf)
print()

df_duf = df.drop_duplicates(subset=['c2', 'c3'], keep=False)
print(df_duf)
print()