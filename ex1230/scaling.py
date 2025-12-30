import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'car name']

print(df.head(3))
df.info()
print()

# df = df[df['horsepower'] != '?']
# df['horsepower'] = df['horsepower'].astype('float')

# df.info()
# print()

df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df = df.dropna(subset=['horsepower'])
df['horsepower'] = df['horsepower'].astype('float')

df.info()
print()

# 1. 'raise' (기본값): 에러를 발생시키고 멈춤
# 2. 'coerce': 숫자로 못 바꾸는 값은 NaN(결측치)으로 강제 변환
# 3. 'ignore': 숫자로 못 바꾸면 그냥 원본 데이터를 그대로 반환

print('\n-------- min-max scaling --------\n')

df['horsepower_minmax'] = MinMaxScaler().fit_transform(df[['horsepower']])
# df['horsepower_minmax'] = (df['horsepower'] - df['horsepower'].min()) / \
#     (df['horsepower'].max() - df['horsepower'].min())

print(df['horsepower_minmax'].head(10))
print()

print('\n-------- standard scaling --------\n')

# df['horsepower_std'] = StandardScaler().fit_transform(df[['horsepower']])
# scaler = StandardScaler()
# df['horsepower_std'] = scaler.fit_transform(df[['horsepower']])
df['horsepower_std'] = (df['horsepower'] - df['horsepower'].mean()) / \
    df['horsepower'].std()
print(df['horsepower_std'].head())
print()