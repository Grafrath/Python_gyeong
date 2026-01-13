import pandas as pd
import matplotlib.pyplot as plt

# 1. 한글 폰트 및 스타일 설정
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')

# 2. 데이터 로드 및 전처리
df = pd.read_excel('./data/남북한발전전력량.xlsx')
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis=1, inplace=True)
df.set_index('발전 전력별', inplace=True)

df = df.T
df = df.replace('-', 0)
df = df.rename(columns={'합계':'총발전량'})

df['총발전량 - 1년'] = df['총발전량'].shift(1)
df['증감률'] = ((df['총발전량']-df['총발전량 - 1년'])/df['총발전량 - 1년']) * 100
df['증감률'] = df['증감률'].fillna(0)
print(df)
print()

# ---------------------------------------------

ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(12,8), width=0.7, stacked=True)
ax2 = ax1.twinx() # x축 공유
ax2.plot(df.index, df['증감률'], ls='--', marker = 'o', markersize=10,
         color='green', label='전년대비 증감률(%)')

ax1.set_ylim(0, 300)
ax1.set_xlabel('연도', size=15)
ax1.set_ylabel('발전량 (억 kWh)', size=15)
ax1.set_title('북한 전력 발전량 (1990 ~ 2016)', size=20)
ax1.legend()
plt.show()