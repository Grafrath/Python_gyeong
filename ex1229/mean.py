import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']


print('\n-------- 평균값 --------\n')

print(df.mean(numeric_only=True))
print()
print(df['mpg'].mean())
print()

print('\n-------- 최댓값 --------\n')
print(df.max(numeric_only=True))
print()
print(df['mpg'].max())
print()

print('\n-------- 최솟값 --------\n')
print(df.min(numeric_only=True))
print()
print(df['mpg'].min())
print()

print('\n-------- 표준편차 --------\n')
print(df.std(numeric_only=True))
print()
print(df['mpg'].std())
print()

print('\n-------- 분산 --------\n')
print(df.var(numeric_only=True))
print()
print(df['mpg'].var())
print()