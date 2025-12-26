import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

exam_data = {'수학':[90, 80, 70, 100, 40], 
             '영어':[88, 77, 66, 95, 35], 
             '음악':[30, 40, 50, 90, 10]}

df = pd.DataFrame(exam_data, index=['철수', '영희', '미진', '보라', '연진'])
print(df)


print("\n======= 원소 반환 =======\n")

df2 = df.loc['철수', '수학']
print(df2)
print(type(df2)) # <class 'numpy.int64'>

df2 = df.iloc[0, 0]
print(df2)


print("\n======= 시리즈 반환 =======\n")

# 철수의 수학, 영어 점수 뽑아보기
# loc, iloc 두가지 경우로!

df3 = df.loc['철수', ['수학', '영어']]
print(df3)
print(type(df3)) # <class 'pandas.core.series.Series'>
print()

df3 = df.iloc[0, [0, 1]]
print(df3)
print(type(df3))


print("\n======= 데이터프레임 반환 =======\n")

# 철수와 미진의 수학, 영어 
# loc, iloc 로 뽑아보기

df4 = df.loc[['철수', '미진'], ['수학', '영어']]
print(df4)
print(type(df4))
print()

df4 = df.iloc[[0, 2], [0, 1]]
print(df4)
print()

# 철수부터 보라까지, 수학이랑 음악 뽑아보기
# loc, iloc

df5 = df.loc['철수':'보라', ['수학', '음악']]
print(df5)
print()

df5 = df.iloc[0:4, [0, 2]]
print(df5)