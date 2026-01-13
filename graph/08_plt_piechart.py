import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 한글 폰트 및 스타일 설정
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'car name']

df['count'] = 1

df_origin = df.groupby('origin').sum(numeric_only=True)
df_origin.index = ['USA', 'EU', 'JAP']

df_origin['count'].plot(kind='pie', figsize=(10, 8),
                        startangle=90, autopct='%1.1f%%',
                        colors=['chocolate', 'bisque', 'cadetblue'],
                        textprops={'fontsize':20})
plt.title('Model Origin', size=30)
plt.axis('equal')
plt.ylabel('')
plt.legend(labels=df_origin.index)
plt.show()