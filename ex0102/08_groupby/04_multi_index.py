import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
df = titanic[['age', 'sex', 'class', 'fare', 'survived']]
print(df)
print()

# class, sex 로 그룹바이
grouped = df.groupby(['class', 'sex'], observed=True)

# mean, std 애그리거트
gdf = grouped.agg(['mean', 'std'], numeric_only=True)
print(gdf)
print()

print(gdf.index)
print()
gdf.info()
print()


# 멀티 인덱스 만들기 - 배열의 리스트를 이용
arrays = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]]
multi_index_arrays = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))
print(multi_index_arrays)
print()


# 멀티 인덱스 만들기 - 튜플의 배열을 이용
tuples = [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
multi_index_tuples = pd.MultiIndex.from_tuples(tuples, names=('letter', 'number'))
print(multi_index_tuples)
print()


# 멀티 인덱스 만들기 - 교차 반복객체를 이용
letter = ['a', 'b']
number = [1, 2]
multi_index_product = pd.MultiIndex.from_product([letter, number],
                                                 names=('letter', 'number'))
print(multi_index_product)
print()


# 멀티 인덱스 만들기 - 데이터프레임을 이용
df = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]], columns=['letter','number'])
print(df)
print()

multi_index_frame = pd.MultiIndex.from_frame(df)
print(multi_index_frame)


print('\n======= 멀티인덱스 추출 =======\n')

# 멀티인덱스 특정 레벨 추출1
print(multi_index_frame.get_level_values(0))
print()

# 멀티인덱스 특정 레벨 추출2
print(multi_index_frame.get_level_values('letter'))


print('\n======= 컬럼의 멀티인덱스 추출 =======\n')

print(gdf)
print()

# 컬럼의 멀티 인덱스 확인
print(gdf.columns.levels)
print()

# 컬럼 멀티인덱스 추출 1
print(gdf.columns.get_level_values(0))
print()

# 컬럼 멀티인덱스 추출 2
print(gdf.columns.get_level_values(1))


print('\n======= 인덱싱 =======\n')

print(gdf['age'])
print()

print(gdf['age']['mean'])
print()

print(gdf['age', 'mean'])
print()

# class 값이 First인 행 선택
print(gdf.loc['First'])
print()

print(gdf.loc[('First', 'female')])
print()

print(gdf.loc[('First', 'female'), 'age'])
print()

print(gdf.loc[('First', 'female'), ('age', 'mean')])
print()

print(gdf)
print()

# first, female 의 age standard 부터 fare standard 까지
print(gdf.loc[('First', 'female'), ('age', 'std'):('fare', 'std')])
print()

print('\n======= class 값이 First인 행 선택 =======\n')

print(gdf.loc['First'])

print('\n======= sex 값이 female인 행 선택 =======\n')

# print(gdf.loc['female']) # 두번째 레벨이라 안된다

# 처음부터 그룹바이를 sex, class 순으로 해서 
# print(gdf.loc['female']) 이게 되게 해보자.

df1 = titanic[['age', 'sex', 'class', 'fare', 'survived']]
grouped1 = df1.groupby(['sex', 'class'], observed=True)
gdf1 = grouped1.agg(['mean', 'std'], numeric_only=True)
print(gdf1.loc['female'])

# index가 class, sex 순서라면 아래와 같이 female 선택 가능
# 교차 섹션(cross-section) 이용
female_class = gdf.xs('female', level='sex')
print(female_class)
print()

# 혹은 아래와 같이 가능
female_class = gdf.loc[(slice(None)), 'female', : ]
print(female_class)


print('\n======= 멀티 인덱스 정렬 =======\n')

print(gdf.sort_index(level=0, ascending=False))
print()

print(gdf.sort_index(level='sex', ascending=False))
print()

print(gdf.sort_index(level=['sex', 'class'], ascending=[False, True]))
print()