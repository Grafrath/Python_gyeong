import pandas as pd
import matplotlib.pyplot as plt

# 1. 한글 폰트 및 스타일 설정
plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')

# 2. 데이터 로드 및 전처리
df = pd.read_excel('graph/시도별_전출입_인구수.xlsx', header=0)
df = df.ffill()

# 서울에서 타지역으로 이동한 데이터 필터링
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask].drop(['전출지별'], axis=1)
df_seoul.set_index('전입지별', inplace=True)

# 3. 분석할 타도시 선택 및 데이터 정제
# 경기도, 강원도, 충청남도, 전라남도로 이동한 데이터만 추출
df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],:]

# 데이터 타입 변환 ('-' -> 0, 문자열 -> 숫자)
df_4 = df_4.replace('-', '0').astype(int)

# 4. 행과 열을 바꿈 (그래프를 그리기 위해 연도가 인덱스로 가야 함)
df_4 = df_4.T

# 면적 그래프 그리기
# stacked=False를 주면 그래프가 겹쳐 보이고, True를 주면 누적되어 쌓입니다.
# stacked = 쌓다 / alpha = 투명도
# figsize=(12,8) 없으면 자동 생성
# df_4.plot(kind='area',stacked=True,alpha=0.7,figsize=(12,8))
# plt.title('서울 -> 타도시', size=20)
# plt.ylabel('이동 인구수', size=20)
# plt.xlabel('기간', size=20)
# plt.legend(fontsize=15)
# plt.show()

# 맷플롭립 방식
# plt.figure(figsize=(12, 6))
# plt.stackplot(df_4.index, df_4.T, alpha=0.2, labels=df_4.columns)
# plt.show()

# # 객체 받아서 그리기
# ax = df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(12, 8))
# ax.set_title('서울 -> 타도시 인구 이동', size=30, color='brown', weight='bold')
# ax.set_ylabel('이동 인구수', size=20, color="#15008d")
# ax.set_xlabel('기간', size=20, color="#8e00cf")
# ax.legend(loc='upper right', fontsize=15)
# plt.show()

# # 맷플롭립 방식 + 객체 받아서 그리기 
# fig, ax = plt.subplots(1, 1, figsize=(12, 8))
# df_4.plot(kind='bar', stacked=True, alpha=0.5, ax=ax)

# ax.set_title('서울 -> 타도시 인구 이동', size=30, color='brown', weight='bold')
# ax.set_ylabel('이동 인구수', size=20, color="#15008d")
# ax.set_xlabel('기간', size=20, color="#8e00cf")
# ax.legend(loc='upper right', fontsize=15)
# ax.set_xticks(range(0, len(df_4.index), 5))
# ax.set_xticklabels(df_4.index[::5], rotation=45)
# plt.show()

# =================================

df = pd.DataFrame({
    "A": [1, 3, 2, 4],
    "B": [4, 2, 3, 1],
    "C": [2, 3, 4, 5]
})

# fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# df['A'].plot(kind='line', ax=ax[0, 0], title='Line A')
# ax[0, 0].set_xlabel('Index')
# ax[0, 0].set_ylabel('Value')

# df['B'].plot(kind='bar', ax=ax[0, 1])
# ax[0, 1].set_title('bar B')
# ax[0, 1].set_xlabel('Index')
# ax[0, 1].set_ylabel('Value')

# df.plot(kind='scatter', ax=ax[1, 0], x='A', y='B')
# ax[0, 1].set_title('scatter A vs B')
# ax[0, 1].set_xlabel('A')
# ax[0, 1].set_ylabel('B')

# plt.show()