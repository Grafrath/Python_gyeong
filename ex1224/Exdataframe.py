'''
데이터 프레임 = 이차원 자료 구조(ex. 엑셀)
데이터 프레임의 각 열은 시리즈 객체
행(row) 열(column)
'''

import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

print('\n-------- 딕셔너리 전환 --------\n')

dict_data = { 'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9]}

df = pd.DataFrame(dict_data)
print(type(df))
print(df)

print('\n-------- 이중리스트 전환 --------\n')

df = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
                  index=['준서', '예은'], columns=['나이', '성별', '학교'])
print(df)
print()

print(df.index)
print(df.columns)
print()

df.index=['학생1', '학생2']
df.columns=['연령', '남여', '소속']
print(df)

print('\n-------- 리네임 --------\n')
df_rename = df.rename(columns={'연령':'age', '남여':'gender'})
print(df_rename)
print()

df.rename(columns={'연령':'age', '남여':'gender'}, inplace=True)
print(df)
print()

df.rename(index={'학생1':'김학생'}, inplace=True)
print(df)

print('\n-------- drop/행삭제 --------\n')

exam_data = { '수학':[90,80,70], '영어':[80,70,90], '음악':[70,60,80] }
df = pd.DataFrame(exam_data, index=['철수','영희','미진'])
print(df)
print()
df1 = df.drop("미진")
print(df1)
print()

df2 = df.drop(["미진",'철수'])
print(df2)
print()

df3 = df.drop('철수', axis=0) # 0 행/ 1 열
print(df3)
print()

df4 = df.drop('철수', axis='index')
print(df4)
print()

df5 = df.drop(index='철수')
print(df5)

print('\n-------- drop/열삭제 --------\n')

exam_data = { '수학':[90,80,70], '영어':[80,70,90], '음악':[70,60,80] }
df = pd.DataFrame(exam_data, index=['철수','영희','미진'])
print(df)

df1 = df.drop('수학', axis=1)
print(df1)
print()

df2 = df.drop(columns=["영어",'음악'])
print(df2)
print()