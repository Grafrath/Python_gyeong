import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

exam_data = { '수학':[90,80,70], '영어':[80,70,90], '음악':[70,60,80] }
df = pd.DataFrame(exam_data, index=['철수','영희','미진'])
print(df)

print('\n-------- 행선택 --------\n')

lb1 = df[0:2]
lb2 = df.head(2)
lb3 = df[df['수학'] >= 80]

print(lb1)
print()
print(lb2)
print()
print(lb3)
print()
print(type(lb1))
print(type(lb2))
print(type(lb3))

lb4 = df.loc[['철수', '미진']]
lb5 = df.iloc[[0,1]]

print(lb4)
print()
print(lb5)
print()

lb6 = df.loc['철수':'영희']
lb7 = df.iloc[0:1]

print(lb4)
print()
print(lb5)
print(type(lb5))

print('\n-------- 열선택 --------\n')

math = df['수학']
print(math)
print(type(math))
print()

eng = df.영어
print(eng)
print(type(eng))
print()

print('\n-------- 고급슬라이싱 --------\n')

exam_data = { '수학':[90,80,70,100,60], '영어':[80,70,90,95,50], '음악':[70,60,80,90,100] }
df = pd.DataFrame(exam_data, index=['철수','영희','미진','보라','연진'])
print(df)
print()

df1 = df.iloc[0:5:2]
print(df1)
print()

df2 = df.iloc[::2]
print(df2)
print()

df2 = df.iloc[::-1]
print(df2)
print()

df2 = df.iloc[0:2]
print(df2)
print()

df2 = df.iloc[0:2,0:2]
print(df2)
print()

df3 = df.iloc[1:3,0:2]
print(df3)
print()
