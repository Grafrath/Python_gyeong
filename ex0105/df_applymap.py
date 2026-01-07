import pandas as pd
import seaborn as sns

print('\n-------- map함수 활용 --------\n')

titanic = sns.load_dataset('titanic')
df = titanic[['age', 'fare']]
print(df.head(5))
print()

def add_10(n):
    return n + 10

def add_two_obf(a, b):
    return a + b

print('\n-------- 데이터 프레임에 map 적용 --------\n')

df_map = df.map(add_10)
print(df_map.head(5))
print()

df_map2 = df.map(add_two_obf, b = 10)
print(df_map2.head(5))
print()

print('\n-------- map 적용(Lambda 함수) --------\n')

df_mapl = df.map(lambda x: x + 10)
print(df_mapl.head(5))
print()

df_mapl2 = df.map(lambda x, b: x + b, b=10)
print(df_mapl2.head(5))
print()

print('\n-------- 데이터 프레임에 apply 적용 --------\n')

def cal_state(col):
    max_val = col.max()
    min_val = col.min()
    mean_val = col.mean()
    median_val = col.median()

    return pd.Series([max_val, min_val, mean_val, median_val], 
                     index=['Max', 'Min', 'Mean', 'Median'])

df_stats = df.apply(cal_state, axis=0)
print(df_stats)
print()

df_stats = df.apply(cal_state, axis=1)
print(df_stats)
print()

result_sr = df.apply(lambda x: 
                     pd.Series([x.max(), x.min()], index=['max', 'min']), axis=1)
print(result_sr)
print()

print('\n-------- apply적용(집계함수) 행전달 --------\n')

def cal_diff(col):
    diff = col.max() - col.min()
    avg = col.mean()

    return pd.Series([diff, avg], 
                     index=['차이', '평균'])

result_sr = df.apply(cal_diff, axis=1)
print(result_sr)
print()

# def cal_diff(col,b):
#     diff = (col.max() - col.min()) * b
#     avg = col.mean()

#     return pd.Series([diff, avg], 
#                      index=['차이', '평균'])

# result_sr = df.apply(cal_diff, b = 2, axis=1)

result_sr = df.apply(lambda col: pd.Series([(col.max() - col.min()) * 2, col.mean()], 
                                          index=['차이', '평균']), axis=1)
print(result_sr)
print()

print('\n-------- apply적용(집계함수) 필터링 --------\n')

fil_col = df.apply(lambda col: col.mean() > 30)
print(fil_col)
print()

filtered_df = df.loc[:,fil_col]
print(filtered_df)
print()

df['High'] = df.apply(lambda row: 'Yes' if row.mean() > 50 else 'No', axis=1)
print(df.head(10))