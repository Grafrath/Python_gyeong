import pandas as pd
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = sns.load_dataset('titanic')
# print(df.head().isnull())
# print()

# not null
# print(df.head().notnull())
# print()

# print(df.isnull().sum(axis=0))
# print()

print('\n======== missingno ========\n')

# 매트릭스
# msno.matrix(df)
# plt.show()

# 막대그래프
# msno.bar(df)
# plt.show()

# 히트맵
# msno.heatmap(df)
# plt.show()

# # 덴드로그램
# msno.dendrogram(df)
# plt.show()