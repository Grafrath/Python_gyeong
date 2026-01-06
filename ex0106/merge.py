import pandas as pd
import seaborn as sns
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 300)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df1 = pd.read_excel('./data/stock_price.xlsx')
df2 = pd.read_excel('./data/stock_valuation.xlsx')

print('\n-------- merge inner --------\n')

# 교집합
merge_inner = pd.merge(df1, df2, how='inner', on='id')
print(merge_inner)
print()

merge_inner2 = pd.merge(df1, df2, how='inner',
                        left_on=['id', 'stock_name'],
                        right_on=['id', 'name'])
merge_inner2.drop('name', axis=1, inplace=True)
print(merge_inner2)
print()

print('\n-------- merge outer --------\n')

# 합집합
merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer)
print()

mergeL = pd.merge(df1, df2, how='left', on='id')
print(mergeL)
print()


mergeR = pd.merge(df1, df2, how='right', on='id')
print(mergeR)
print()

price = df1[df1['price'] < 5000]
print(price)
print()

value = pd.merge(price, df2, on='id')
print(value)
print()

value1 = pd.merge(df1[['id', 'stock_name', 'value', 'price']],
                 df2['id'],
                 on='id',
                 how='inner')
print(value1)
print()

value2 = pd.merge(df1, df2, on='id').query('price < 5000')
print(value2)
print()

print('\n-------- 병합 --------\n')

sdf1 = pd.DataFrame({
    'employee': ['Alice', 'Sam', 'Eva'], 
    'department': ['HR', 'Tech', 'HR']
})

sdf2 = pd.DataFrame({
    'department': ['HR', 'Tech', 'Finance'],
    'manager': ['John', 'Jane', 'Kim']
})

sdf4 = pd.DataFrame({
    'department': ['HR', 'HR', 'Tech', 'Tech', 'Finance'],
    'task': ['recruiting', 'payroll', 'development', 'support', 'budgeting']
})

result_1 = pd.merge(sdf1, sdf2, on='department')
print(result_1)
print()

result_2 = pd.merge(sdf1, sdf4, on='department')
print(result_2)
print()