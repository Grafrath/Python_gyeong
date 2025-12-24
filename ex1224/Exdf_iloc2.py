import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

exam_data = { '수학':[90,80,70], '영어':[80,70,90], '음악':[70,60,80] }
df = pd.DataFrame(exam_data, index=['철수','영희','미진'])
print(df)
print()

print('\n-------- 원소 반환 --------\n')

lb1 = df.loc['철수', '수학']
print(lb1)
print(type(lb1))
print()

lb2 = df.iloc[0,0]
print(lb2)
print(type(lb2))
print()

print('\n-------- 시리즈 반환 --------\n')

lb3 = df.iloc[0,[0,1]]
print(lb3)
print(type(lb3))
print()

print('\n-------- 데이터 프레임 반환 --------\n')

exam_data = { '수학':[90,80,70,100,60], '영어':[80,70,90,95,50], '음악':[70,60,80,90,100] }
df = pd.DataFrame(exam_data, index=['철수','영희','미진','보라','연진'])

lb4 = df.loc[['철수','미진'],['수학','영어']]
print(lb4)
print(type(lb4))
print()

lb5 = df.iloc[0:4,[0,2]]
print(lb5)
print(type(lb5))
print()