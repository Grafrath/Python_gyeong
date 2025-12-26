# 터미널에 pip install pandas

import pandas as pd

# 시리즈 = 인덱스와 데이터

print("\n======= 리스트를 시리즈로 =======\n")

list_data = ['a', 2, 'b']

sr = pd.Series(list_data)
print(sr)
print(sr.index)
print(sr.values)
print(type(sr)) 
print(sr.dtype)
print(len(sr))
print(sr.shape)
print(sr.ndim)


print("\n======= 튜플을 시리즈로 =======\n")

tup_data = ('영민', '남', True)
sr2 = pd.Series(tup_data, index=['이름', '성별', '학생여부'])
print(sr2)
print(sr2['이름']) # 영민
print(sr2[1 : 2])
print(sr2[0 : 2])
print(sr2.index)
print(sr2.iloc[0]) # 영민
print(sr2[0]) # 영민 but 경고...
print(sr2.iloc[1 : 2]) # 별다른 경고 X


print("\n======= 시리즈 생성 =======\n")

print(pd.Series())
print()
print(pd.Series(5))
print()
print(pd.Series(5, index=['a', 'b', 'c']))
print()

print(pd.Series([1, 2, 3]).dtype) # int64
print(pd.Series([1.0, 2.0]).dtype) # float64
print(pd.Series(['a', 'b']).dtype) # object
print(pd.Series(['a', 2]).dtype)
print(pd.Series(['a', 'b'], dtype='string').dtype) # string

'''
Pandas는 numpy를 기반으로 만들어졌다.
numpy -- 파이썬에서 과학 계산 등 숫자 계산에 특화된 라이브러리
int64, float64는 넘피의 숫자형 (데이터타입)
'''