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

# sr_one = df_seoul.loc['경기도']
# df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], '2010':'2017']
# df_4 = df_4.T

# plt.style.use('Solarize_Light2')

# df_4.plot(kind='bar',figsize=(12,8), width=0.5, color=['orange', 'green', 'skyblue', 'blue'])
# plt.title('서울 -> 타도시', size=20, pad=10, color='brown', weight='bold')
# plt.ylabel('이동 인구수', size=20, labelpad=10)
# plt.xlabel('기간', size=20, labelpad=10)
# plt.ylim(5000, 30000)
# plt.legend(fontsize=15)
# plt.show()

df_4['합계'] = df_4.sum(axis=1)
df_total = df_4[['합계']].sort_values(by='합계', ascending=True)

# df_total.plot(kind='bar',figsize=(12,8))
# plt.title('서울 -> 타도시', size=20, pad=10, color='brown', weight='bold')
# plt.ylabel('이동 인구수', size=20, labelpad=10)
# plt.xlabel('기간', size=20, labelpad=10)
# plt.show()

df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], '2010':'2017']
df_4 = df_4.replace('-', '0').astype(int)

df_4['합계'] = df_4.sum(axis=1)
df_total = df_4[['합계']].sort_values(by='합계', ascending=True)

# df_sum = df_target.sum(axis=1)

# plt.figure(figsize=(12, 8))
# ax = df_sum.plot(kind='bar', color=['#f39c12', '#27ae60', '#3498db', '#e74c3c'], rot=0)

# for i, v in enumerate(df_sum):
#     ax.text(i, v + 500, f'{v:,}', ha='center', va='bottom', fontsize=12, fontweight='bold')

# plt.title('서울 -> 타도시', size=22, weight='bold', pad=20)
# plt.xlabel('전입 지역', size=15)
# plt.ylabel('총 이동 인구수 (명)', size=15)

# plt.ylim(0, df_sum.max() * 1.15)

# plt.show()

# fig, axes = plt.subplots(1, 2, figsize=(12, 8))
# axes[0].barh(df_total.index, df_total['합계'])
# axes[0].set_title('시도별 전입인구')

# df_total.plot(kind='barh', ax=axes[1])
# axes[1].set_title('시도별 전입인구')

# plt.tight_layout()
# plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 8))
axes[0].barh(df_total.index, df_total['합계'])
axes[0].set_title('시도별 전입인구')

df_total.plot(kind='barh', ax=axes[1])
axes[1].set_title('시도별 전입인구')
axes[1].set_xticklabels(['충남', '경북', '강원', '전남'], rotation=45)

plt.tight_layout()
plt.show()