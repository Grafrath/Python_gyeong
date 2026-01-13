import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# df = sns.load_dataset('tips')

# sns.boxplot(x='day', y='tip', data=df)
# plt.title('Tips by Day')
# plt.show()

data = {'Sales': [10, 20, 15, 25, 30], 'Expenses': [5, 15, 10, 20, 25]}
df = pd.DataFrame(data)

df.plot(kind='line')
plt.show()

# plt.plot(data['Sales'], label='Sales')
# plt.plot(data['Expenses'], label='Expenses')

# plt.legend()
# plt.show()