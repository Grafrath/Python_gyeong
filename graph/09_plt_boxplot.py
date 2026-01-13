import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 한글 폰트 및 스타일 설정
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('grayscale')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'car name']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))

ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA', 'EU', 'JPN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA', 'EU', 'JPN'], vert=False)
ax1.set_title('제조국가별 연비 (수직박스 Plot)')
ax2.set_title('제조국가별 연비 (수평박스 Plot)')
plt.tight_layout()
plt.show()

'''
가운데 선 - 중앙값 (median)
박스 아래/위 - Q1, Q3
박스 아래 끝 - 1사분위수 (Q1): 하위25%
박스 위 끝 - 3사분위수 (Q3): 상위 75%

수염(whisker) - 일반적인 범위
IQR = Q3 - Q1
Q1 - 1.5 x IQR ~~~ Q3 + 1.5 x IQR
'''

fig, axes = plt.subplots(1, 2, figsize=(12,6))
df.plot(kind='box', column=['mpg'], by=['origin'], ax=axes[0])
axes[0].set_title('제조국가별 연비 (수직박스 플롯)', size=15)

axes[1].boxplot(x=[df[df['origin']==1]['mpg'],
                   df[df['origin']==2]['mpg'],
                   df[df['origin']==3]['mpg']],
                labels=['USA', 'EU', 'JPN'], vert=False)
axes[1].set_title('제조국가별 연비 (수평박스 플롯)', size=15)

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12,6))
df.plot(kind='box', column=['mpg'], by=['origin'], ax=axes[0])
axes[0].set_title('제조국가별 연비 (수직박스 플롯)', size=15)

axes[1].boxplot(x=[df[df['origin']==1]['mpg'],
                   df[df['origin']==2]['mpg'],
                   df[df['origin']==3]['mpg']],
                labels=['USA', 'EU', 'JPN'], vert=False)
axes[1].set_title('제조국가별 연비 (수평박스 플롯)', size=15)

plt.tight_layout()
plt.suptitle('')
plt.show()