import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)


students = {'이름':['서준', '우현', '인아'],
            '수학':[90, 80, 70], 
            '영어':[88, 77, 66], 
            '사회':[30, 40, 50],
            '체육':[10, 20, 30]}

df = pd.DataFrame(students)
print(df)


print("\n======= 인덱스 지정 =======\n")

ndf = df.set_index('이름')
print(ndf)
print()

ndf2 = df.set_index(['이름'])
print(ndf2)
print()

ndf3 = ndf2.set_index('수학')
print(ndf3)
print()

ndf4 = ndf3.set_index('영어')
print(ndf4)
print()

ndf5 = ndf2.set_index(['수학', '영어'])
print(ndf5)
print()


print("\n======= 인덱스 재배열 =======\n")

df = pd.DataFrame(students, index=['s1', 's2', 's3'])
print(df)
print()

new_index = ['s1', 's2', 's3', 's4', 's5']

ndf = df.reindex(new_index)
print(ndf)
print()

# s4, s5 의 수학 점수 80, 90
ndf.loc[['s4', 's5'], '수학'] = [89, 90]
print(ndf)
print()


ndf = df.reindex(new_index, fill_value=80)
print(ndf)


print("\n======= 인덱스/컬럼 재배열 =======\n")

ndf = df.reindex(index=new_index, columns=['이름', '수학', '영어', '과학'])
print(ndf)


print("\n======= reindex 이용한 자리 바꾸기 =======\n")

print(df)
print()

# reindex 사용해서 순서를 이름, 영어, 수학, 사회, 체육

ndf = df.reindex(columns=['이름', '영어', '수학', '사회',' 체육'])
print(ndf)
print()


print("\n======= NaN 채우기 =======\n")

ndf = df.reindex(new_index)
print(ndf)
print()

ndf = ndf.fillna(0)
print(ndf)
print()

ndf = ndf.astype({'수학':'int64', '영어':'int64'})
print(ndf)
print()
ndf.info()


print("\n======= 인덱스 초기화 =======\n")

print(df)
print()

ndf = df.reset_index()
print(ndf)
print(ndf.shape)
print(ndf.columns)
print(ndf.columns.tolist())
print()

ndf = df.reset_index(names=['id'])
print(ndf)
print()

ndf = df.reset_index(drop=True)
print(ndf)


print("\n======= 인덱스 기준으로 정렬 =======\n")

ndf = df.sort_index(ascending=False)
print(ndf)
print()

ndf = df.sort_index(ascending=True)
print(ndf)


print("\n======= 특정 컬럼 기준으로 정렬 =======\n")

ndf = df.sort_values(by='수학', ascending=True)
print(ndf)
print()

ndf = df.sort_values(by='수학', ascending=False)
print(ndf)
print()


# s1, 수학 ===> 80 점
ndf.loc['s1', '수학'] = 80
print(ndf)
print()

ndf = ndf.sort_values(by=['수학', '사회'], ascending=False)
print(ndf)
print()