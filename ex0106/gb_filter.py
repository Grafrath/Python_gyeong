import pandas as pd
import seaborn as sns
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'], observed=True)
grouped_head = grouped.head(3)
print(grouped)
print()
print(grouped_head)
print()

grouped_first = grouped.nth(175)
print(grouped_first)
print()

print(grouped[['age', 'survived']].nth(175))
print()

grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter)
print()

for key, group in grouped:
    print('key: ', key)
    print('number: ', len(group))
    print(group.head())
    print()

grouped_age = grouped.filter(lambda x: x['age'].mean() < 30)
print(grouped_age)
print()