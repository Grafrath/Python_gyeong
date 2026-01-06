import pandas as pd

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

print('\n======= pd.concat =======\n')

# 2개의 데이터프레임을 세로로 붙이기
result1 = pd.concat([df1, df2])
print(result1)
print()

# 정수 인덱스를 새로 부여
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2)
print()

# join='inner' 옵션 적용 (교집합)
result2_in = pd.concat([df1, df2], ignore_index=True, join='inner')
print(result2_in) # 디폴트 'outer'
print()

# 데이터를 가로로 붙이기
result3 = pd.concat([df1, df2], axis=1)
print(result3)
print()

# 가로 붙이기 join='inner' 적용
result3_in = pd.concat([df1, df2], axis=1, join='inner')
print(result3_in)
print()

# 시리즈 만들기
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')
sr4 = pd.Series(['a6', 'b6', 'c6', 'd6'], index=['a', 'b', 'c', 'd'])

print(sr1)
print()

result4 = pd.concat([df1, sr1], axis=1)
print(result4)
print()

result5 = pd.concat([df2, sr2], axis=1)
print(result5)
print()

print(sr4)
print(df2)

result5 = pd.concat([df2, sr4], axis=1)
print(result5)
print()

print(sr4.to_frame())
print()
print(sr4.to_frame().T)
print()

result6 = pd.concat([df2, sr4.to_frame().T], ignore_index=True)
print(result6)
print()

result7 = pd.concat([sr1, sr3], axis=1)
print(result7)
print()

result8 = pd.concat([sr1, sr3], axis=0)
print(result8)


print('\n======= 3개 이상 concat =======\n')
