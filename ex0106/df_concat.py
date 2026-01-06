import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3])

print(df1)
print()

df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5])

print(df2)
print()

print('\n-------- pd.concat --------\n')

result1 = pd.concat([df1, df2])
print(result1)
print()

result2 = pd.concat([df1, df2], ignore_index=True)
print(result2)
print()

result2_in = pd.concat([df1, df2], ignore_index=True, join='inner')
print(result2_in)
print()

result3 = pd.concat([df1, df2], axis=1)
print(result3)
print()

result3_in = pd.concat([df1, df2], axis=1, join='inner')
print(result3_in)
print()

print('\n-------- 시리즈 concat --------\n')

sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
print(sr1)
print()

sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')
sr4 = pd.Series(['a6', 'b6', 'c6', 'd6'], index=['a', 'b', 'c', 'd'])

result4 = pd.concat([df1, sr1], axis=1)
print(result4)
print()

result5 = pd.concat([df2, sr2], axis=1)
print(result5)
print()

print('\n-------- concat 3개 --------\n')

result = pd.concat([df2, sr1], axis=1, ignore_index=True)
print(result)
print()

result = pd.concat([df1, sr3], axis=1, ignore_index=True, join='inner')
print(result)
print()

result = pd.concat([df2, sr4], axis=1, ignore_index=True, join='outer')
print(result)
print()
