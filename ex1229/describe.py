import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

print(df.head())
print()

df.info()
print()
print(df.dtypes)
print()

print('\n-------- 산술정보 --------\n')

print(df.describe())
print()
print(df.describe(include='object'))
print()
print(df.count())
print()

uv = df['origin'].value_counts()
print(uv)
print()

uv = df['origin'].value_counts(normalize=True)
print(uv)
print()

uv = (df['origin'].value_counts(normalize=True) * 100).round(1)
print(uv)
print()