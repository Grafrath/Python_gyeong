import pandas as pd
import numpy as np
# from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'car name']

df.info()
print()

df = df[df['horsepower'] != '?']
df['horsepower'] = df['horsepower'].astype('float64')
df.info()
print()

print('\n-------- 구간나누기 --------\n')

count, bin_div = np.histogram(df['horsepower'], bins=[50, 100, 200, 300])
print(count)
print()
print(bin_div)
print()
print(df.describe())
print()

# mask = df[df['horsepower'] < 100]
# print(mask)

print('\n-------- cut --------\n')

bin_name = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins=bin_div,
                      labels=bin_name,
                      include_lowest=True)

df = df.dropna(subset=['hp_bin'])

print(df[['car name', 'horsepower', 'hp_bin']].head(10))
df.info()
print()

print('\n-------- 더미변수 --------\n')

hp_dummi = pd.get_dummies(df['hp_bin'], dtype=float)
print(hp_dummi.head(3))
print()

hp_dummi = pd.get_dummies(df['hp_bin'], dtype=float, drop_first=1)
print(hp_dummi.head(3))
print()

print('\n-------- 레이블 인코더 --------\n')

# # 넘피어레이로
# label_en = preprocessing.LabelEncoder()
# one_labeled = label_en.fit_transform(df['hp_bin'])
# # print(one_labeled)
# print(type(one_labeled))
# print()

# # 시리즈로
# one_labeled = pd.Series(label_en.fit_transform(df['hp_bin']))
# # print(one_labeled)
# print(type(one_labeled))
# print()

# # 시리즈를 컬럼에 추가
# df['hp_bin_lb'] = one_labeled
# df.info()
# print(df.sample(3))
# print()

df['hp_bin_lb'] = LabelEncoder().fit_transform(df['hp_bin'])
df.info()
print(df.sample(5))
print()

print('\n-------- 원핫 인코더 --------\n')

one_en = OneHotEncoder(sparse_output=False)
one_fitted = one_en.fit_transform(df[['hp_bin']])
print(one_fitted)
print(type(one_fitted))
print()

encoded_df = pd.DataFrame (
    one_fitted,
    columns=one_en.get_feature_names_out(['hp_bin'])
)
print(encoded_df)
print()