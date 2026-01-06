import pandas as pd
import seaborn as sns
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
grouped = df.groupby(['class', 'sex'], observed=True)

gdf = grouped.agg(['mean', 'std'], numeric_only=True)
print(gdf)
print()

print(gdf.index)
print()

arrays = [['a', 'a', 'b', 'b'],[1, 2, 1, 2]]
multi_index_arr = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))
print(multi_index_arr)
print()

tuples = [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
multi_index_tup = pd.MultiIndex.from_tuples(tuples, names=('letter', 'number'))
print(multi_index_tup)
print()

letter = ['a', 'b']
number = [1, 2]
multi_index_product = pd.MultiIndex.from_product([letter, number], names=('letter', 'number'))
print(multi_index_product)
print()

df = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]], columns=[letter, number])
print(df)
print()

multi_index_frame = pd.MultiIndex.from_frame(df, names=('letter', 'number'))
print(multi_index_frame)
print()

print('\n-------- 멀티인덱스 추출 --------\n')

print(multi_index_frame.get_level_values(0))
print()

print(multi_index_frame.get_level_values('letter'))
print()

print('\n-------- 컬럼 멀티인덱스 추출 --------\n')

print(gdf.columns.levels)
print()

print(gdf.columns.get_level_values(0))
print()

print('\n-------- 인덱싱 --------\n')

print(gdf['age'])
print()

print(gdf['age']['mean'])
print()

print(gdf['age', 'mean'])
print()

print(gdf.loc['First']['age'])
print()

print(gdf.loc['First','female']['age'])
print()

print(gdf.loc[('First', 'female'), [('age', 'mean'), ('fare', 'mean'), ('fare', 'std')]])
print()

print('\n-------- sex값이 female인 행 --------\n')

print(gdf.loc[[('First', 'female'), ('Second', 'female'), ('Third', 'female')]])
print()

female_class = gdf.xs('female', level='sex')
print(female_class)
print()

female_class = gdf.loc[(slice(None), 'female'), :]
print(female_class)
print()

print('\n-------- 멀티 인덱싱 정렬 --------\n')

print(gdf.sort_index(level=0, ascending=False))
print()

print(gdf.sort_index(level='sex', ascending=False))
print()

print(gdf.sort_index(level=['sex', 'class'], ascending=[False, True]))
print()
