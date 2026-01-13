import pandas as pd
import matplotlib.pyplot as plt

# 1. 한글 폰트 및 스타일 설정
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)
plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'car name']

plt.figure(figsize=(10,6))
plt.hist(df['mpg'], bins=10, color='coral', edgecolor='black')
plt.title('histogram')
plt.xlabel('mpg')
plt.show()

df.plot(kind='scatter', x='weight', y='mpg', color='skyblue', alpha=0.5, figsize=(10,6))
plt.title('중량 vs 연비 산점도', size=15)
plt.show()

df[['mpg', 'origin']].plot(by=['origin'], kind='hist',
                           figsize=(10,6), layout=(3, 1),
                           color='coral',  edgecolor='black', sharex=True)
plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 6))
ax1.hist(df[df['origin']==1]['mpg'], bins=10, color="#267402", edgecolor='black')
ax2.hist(df[df['origin']==2]['mpg'], bins=10, color="#06b874", edgecolor='black')
ax3.hist(df[df['origin']==3]['mpg'], bins=10, color="#c24e00", edgecolor='black')
plt.show()

df[['mpg', 'origin', 'cylinders']].plot(by=['origin'], kind='hist',
                           figsize=(8,30), layout=(3, 1),
                           color='coral',  edgecolor='black', sharex=True)
plt.show()

'''# 한 피규어에 4개 동시에 보여주기
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# [0, 0] - 연비 히스토그램 (분포 확인)
axes[0, 0].hist(df['mpg'], bins=15, color='coral', edgecolor='black')
axes[0, 0].set_title('1. 연비(MPG) 분포', size=15)
axes[0, 0].set_xlabel('mpg')

# [0, 1] - 중량 vs 연비 산점도 (상관관계 확인)
axes[0, 1].scatter(df['weight'], df['mpg'], color='skyblue', alpha=0.5)
axes[0, 1].set_title('2. 중량 vs 연비 상관관계', size=15)
axes[0, 1].set_xlabel('weight')
axes[0, 1].set_ylabel('mpg')

# [1, 0] - 제조국가별 연비 박스 플롯 (그룹별 비교)
# boxplot은 리스트 형태로 데이터를 넣어주면 편리합니다.
origin_list = [df[df['origin']==1]['mpg'], 
               df[df['origin']==2]['mpg'], 
               df[df['origin']==3]['mpg']]
axes[1, 0].boxplot(origin_list, labels=['USA', 'EU', 'JPN'])
axes[1, 0].set_title('3. 국가별 연비 비교 (Box Plot)', size=15)

# [1, 1] - 실린더 수 비중 (파이 차트)
# cylinders_counts = df['cylinders'].value_counts()
# axes[1, 1].pie(cylinders_counts, labels=cylinders_counts.index, autopct='%1.1f%%', 
#                startangle=90, colors=plt.cm.Paired.colors)
# axes[1, 1].set_title('4. 실린더 개수 비중', size=15)

# 전체 레이아웃 조정 및 제목
plt.suptitle('자동차 데이터 분석 종합 리포트', size=25, weight='bold', y=0.95)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()'''