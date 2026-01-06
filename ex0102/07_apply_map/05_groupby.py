import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

print(df.head())


print('\n======= class열 groupby =======\n')

grouped = df.groupby(['class'], observed=True)
print(grouped)
print()

for key, group in grouped:
    print('key :', key)
    print('number :', len(group))
    print(group.head())
    print()

print()

print('\n======= 연산 메서드 적용 =======\n')
averge = grouped.mean(numeric_only=True)
print(averge)
print()

group2 = grouped.get_group(('Third',))
print(group2.head())


print('\n======= 두개 조건으로 groupby =======\n')

group_two = df.groupby(['class', 'sex'], observed=True)

for key, group in group_two:
    print('key :', key)
    print('number :', len(group))
    print(group.head())
    print()

print()

# 각 그룹의 평균 
average_two = group_two.mean(numeric_only=True)
print(average_two)
print()

# groupby 로 'Third'-'female' 만 뽑기
group3 = group_two.get_group(('Third', 'female'))
print(group3.head())
print()


# 필터링으로 'Third', 'female' 만 뽑기
# print( (df['class'] == 'Third') & (df['sex'] == 'female') )

group4 = df[ (df['class'] == 'Third') & (df['sex'] == 'female') ] 
print(group4.head())
print()



print('\n======= observed=True / False =======\n')

import pandas as pd

df = pd.DataFrame({
    'class': pd.Categorical(['A', 'A', 'B'], categories=['A', 'B', 'C']),
    'value': [10, 20, 30]
})

print(df)

group_false = df.groupby('class', observed=False).sum()
print(group_false)
print()

group_true = df.groupby('class', observed=True).sum()
print(group_true)
print()

df.info()