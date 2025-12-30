import pandas as pd
import numpy as np

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'car name']

print(df.head(3))
print()

df['kpl'] = df['mpg'] * 1.61/3.78
print(df['kpl'].head(3))
print()

df['kpl'] = df['kpl'].round(2)
print(df['kpl'].head(3))
print()

df['horsepower'].unique()
df.info()
print()

# df['horsepower'] = df['horsepower'].replace('?', np.nan)
# df = df.dropna(subset=['horsepower'], axis=0)
# df = df[df['horsepower'] != '?']
# df['horsepower'] = df['horsepower'].astype('float')
# df.info()
# print()

print('\n-------- 자료형변환 --------\n')
#origin 컬럼의 고유값
print(df['origin'].unique())
df['origin'] = df['origin'].astype('category')
print(df.dtypes)

'''
object -- 행마다 문자열 전체 저장, 메모리 낭비
category -- 내부적으로 정수코드로 저장, 실제 값은 별도 보관
연산 속도 향상/ 순서가 있는 범주표현 가능
'''

print('\n------------------------\n')

df_grade = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'grade' : ['A', 'B', 'C', 'D', 'F ']
})

print(df_grade)
print()
df_grade.info()
print()

df_grade['grade'] = pd.Categorical(
    df_grade['grade'],
    categories=['F', 'D', 'C', 'B', 'A'],
    ordered=True
)

df_grade.info()
print()

df_grade = df_grade[df_grade['grade'] >= 'C']
print(df_grade)
print()

print('\n------------------------\n')

print(df['model year'].sample(3))
print()
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
print()