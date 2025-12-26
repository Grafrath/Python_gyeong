# 데이터 프레임 = 이차원 자료구조 (ex. 엑셀)
# 데이터프레임의 각 열은 시리즈 객체이다.
# 행(row), 열(column)

import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)



print("\n======= 딕셔너리를 데이터프레임으로 =======\n")

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9]}

df = pd.DataFrame(dict_data)

print(type(df))
print()
print(df)


print("\n======= 이중 리스트를 데이터프레임으로 =======\n")

df2 = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']])
print(df2)
print()

df2 = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])
print(df2)
print()

print(df2.index)
print(df2.columns)
print()

df2.index=['학생1', '학생2']
df2.columns=['연령', '남녀', '소속']
print(df2)



print('\n======= rename =======\n')
df2_rename1 = df2.rename(columns={'연령':'age', '남녀':'gender'})
print(df2_rename1)
print()


df2.rename(columns={'연령':'age', '남녀':'gender'}, inplace=True)
# df2 = df2.rename(columns={'연령':'age', '남녀':'gender'})
print(df2)
print()

# 학생1 ==> '김학생' 바꿔보세요
df2.rename(index={'학생1':'김학생'}, inplace=True)
print(df2)


print('\n======= drop ======\n')

exam_data = {'수학':[90, 80, 70], '영어':[88, 77, 66], '음악':[30, 40, 50]}

df = pd.DataFrame(exam_data, index=['철수', '영희', '미진'])
print(df)


print('\n======= drop / 행삭제 =======\n')

df1 = df.drop('미진')
print(df1)
print()

df2 = df.drop(['철수', '미진'])
print(df2)
print()

df3 = df.drop('철수', axis=0) # 0 행 / 1 열
print(df3)
print()

df4 = df.drop('철수', axis='index') 
print(df4)
print()

df5 = df.drop(index=['철수', '미진']) 
print(df5)


print('\n======= drop / 열삭제 =======\n')

print(df)
print()


df2 = df.drop('수학', axis=1)
print(df2)
print()

df3 = df.drop(['수학', '영어'], axis=1)
print(df3)
print()

print(df3.ndim) # 2
print(df3.shape) # (3, 1)
print(type(df3)) # DataFrame
print()

df4 = df.drop('수학', axis='columns')
print(df4)
print()

df5 = df.drop(columns=['수학'])
print(df5)
print()