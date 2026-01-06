import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
df.info()
print()

print('\n-------- class열 groupby --------\n')

grouped = df.groupby(['class'])

for key, group in grouped:
    print('key: ', key)
    print('number: ', len(group))
    print(group.head())
    print()

print('\n-------- 연산 메서드 적용 --------\n')

averge = grouped.mean(numeric_only=True)
print(averge)
print()

print('\n-------- 두조건으로 groupby --------\n')

group_two = df.groupby(['class', 'sex'], observed=True)

for key, group in group_two:
    print('key: ', key)
    print('number: ', len(group))
    print(group.head())
    print()

print('\n-------- 두조건으로 연산 메서드 적용 --------\n')

average_two = group_two.mean(numeric_only=True)
print(average_two.unstack())
print()

third_female = group_two.get_group(('Third', 'female'))
print(third_female.head(3))
print()

fil_grpup = df[(df['class'] == 'Third') & (df['sex'] == 'female')]
print(fil_grpup.head(3))
print()

group_false = df.groupby('class', observed=False).sum()
print(group_false)
print()

group_true = df.groupby('class', observed=True).sum()
print(group_true)
print()