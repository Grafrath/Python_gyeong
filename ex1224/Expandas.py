import pandas as pd

print('\n-------- 리스트를 시리즈로 --------\n')

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

print('\n-------- 튜플을 시리즈로 --------\n')

tup_data = ['영민', '남', True]

sr = pd.Series(tup_data, index=['이름', '성별', '학점'])
print(sr)
print(sr['이름'])
print(sr.index)
print(sr[0])
print(sr.iloc[0])
print(sr[1:2])
print(sr[0:2])
print(sr.iloc[0:2])

print('\n-------- 시리즈 생성 --------\n')

print(pd.Series())
print()
print(pd.Series(5))
print()
print(pd.Series(5, index=['a', 'b', 'c']))
print()

print(pd.Series([1,2,3]).dtype)
print(pd.Series([1.0, 2.0]).dtype)
print(pd.Series(['a', 'b']).dtype)
print(pd.Series(['a', 2]).dtype)
print(pd.Series(['a', 'b'], dtype='string').dtype)