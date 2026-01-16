import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

titanic = sns.load_dataset('titanic')

sns.countplot(x="class", data=titanic)
plt.title("각 클래스별, 승객 수")
plt.show()