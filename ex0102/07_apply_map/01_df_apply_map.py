import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic[['age', 'fare']]
print(df.head())

def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b


print('\n======= 데이터프레임에 map 적용 =======\n')

df_map = df.map(add_10) # apply도 가능
print(df_map.head())

df_map2 = df.map(add_two_obj, b=10)
print(df_map2.head())



print('\n======= map 적용 (lambda 함수) =======\n')

df_map3 = df.map(lambda n: n + 10)
print(df_map3.head())
print()

df_map4 = df.apply(lambda a, b: a + b, b=10)
print(df_map4.head())
print()


print('\n======= 데이터프레임에 apply 적용(집계함수) =======\n')

def calculate_stats(col):
    max_val = col.max()
    min_val = col.min()
    mean_val = col.mean()
    median_val = col.median()

    return pd.Series([max_val, min_val, mean_val, median_val], index=['Max', 'Min', 'Mean', 'Median'])

# 0 행 1 열
result_df_0 = df.apply(calculate_stats, axis=0) # map은 안됨.
print(result_df_0)
print()

result_df_1 = df.apply(calculate_stats, axis=1)
print(result_df_1)
print()

# 각 열의 (최대-최소) 값. (람다로.)
result_sr = df.apply(lambda x: x.max() - x.min(), axis=0)
print(result_sr)

print('\n======= apply 적용(집계함수) 행전달 =======\n')

# 각 행에 대해 최댓값과 최솟값의 차이와 평균을 반환
def calculate_diff_avg(row):
    diff = row.max() - row.min()
    avg = row.mean()
    return pd.Series([diff, avg], index=['차이', '평균'])

result_df2 = df.apply(calculate_diff_avg, axis=1)
print(result_df2)

# 각 행에 대해 (최댓값-최솟값) * multi, 각 행의 평균     을 반환하는..
# index=['차이', '평균']   # multi = 2
# 요거를 람다로 응용.

result_df3 = df.apply(lambda row, multi: pd.Series([(row.max() - row.min()) * multi, row.mean()], 
                                                   index=['차이', '평균']), multi = 2, axis=1)
print(result_df3)


print('\n======= apply 적용(집계함수) 필터링 =======\n')

# 평균값이 30을 초과하는 열만 필터링
filtered_columns = df.apply(lambda x: x.mean() > 30) # axis=0 생략
print(filtered_columns)
print()

filtered_df = df.loc[:, filtered_columns]
print(filtered_df)
print()

# df의 각 행의 평균이 50을 초과하면 'Yes' 아니면 'No' 인 컬럼 'High' 만들기
# apply, lambda 사용

df['High'] = df.apply(lambda row: 'Yes' if row.mean() > 50 else 'No', axis=1)
print(df)