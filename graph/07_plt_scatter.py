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

# df.plot(kind='scatter', x='weight', y='mpg', color='skyblue', s=10, figsize=(10,6))
# plt.title('중량 vs 연비 산점도', size=15)
# plt.show()

# plt.figure(figsize=(10,8))
# sns.scatterplot(data=df, x='weight', y='mpg',
#                 c='coral', s=40, palette='Set2')
# plt.title('중량 vs 연비 산점도', size=15)
# plt.show()

# 버블 차트

cylinders_size = (df['cylinders'] / df['cylinders'].max()) * 300
# df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10,8),
#         s=cylinders_size, alpha=0.3)
# plt.title('중량 vs 연비 산점도', size=15)
# plt.show()# 