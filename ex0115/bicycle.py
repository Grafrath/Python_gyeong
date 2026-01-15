import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns


plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.unicode.east_asian_width', True)

# 따릉이 데이터 통합
file_list = glob.glob('서울특별시 공공자전거 대여이력 정보_*.csv')
cols = ['대여일시', '이용시간(분)', '이용거리(M)']

bike_list = []
for file in file_list: 
    temp_df = pd.read_csv(file, encoding='cp949', usecols=cols)
    temp_df = temp_df[(temp_df['이용시간(분)'] > 0) & (temp_df['이용거리(M)'] > 0)]
    bike_list.append(temp_df)
    

bike_df = pd.concat(bike_list, ignore_index=True)
bike_df['대여일시'] = pd.to_datetime(bike_df['대여일시'])
bike_df['date'] = bike_df['대여일시'].dt.date
bike_df['hour'] = bike_df['대여일시'].dt.hour

# 시간대별 집계
rentals = bike_df.groupby(['date', 'hour']).agg({
    '대여일시': 'count',
    '이용시간(분)': 'mean',
    '이용거리(M)': 'mean'
}).rename(columns={'대여일시': 'rent_count'}).reset_index()

rentals['date'] = pd.to_datetime(rentals['date'])

# 엑셀파일 불러오기
temp_file = '월별기온.xlsx'
rain_file = '월별강수일.xlsx'

df_temp = pd.read_excel(temp_file)
df_rain = pd.read_excel(rain_file)

# 컬럼명 앞뒤 공백 제거
df_temp.columns = df_temp.columns.str.strip()
df_rain.columns = df_rain.columns.str.strip()

# 날짜 데이터 변환
df_temp['date'] = pd.to_datetime(df_temp['날짜'])
df_rain['date'] = pd.to_datetime(df_rain['일시'])

# 기상 데이터 통합
weather_daily = pd.merge(
    df_temp[['date', '평균기온(℃)']], 
    df_rain[['date', '강수량(mm)']], 
    on='date', how='left'
)

weather_daily['강수량(mm)'] = weather_daily['강수량(mm)'].fillna(0)

#최종 데이터 병합
final_df = pd.merge(rentals, weather_daily, on='date', how='left')

final_df['is_rainy'] = final_df['강수량(mm)'].apply(
    lambda x: 'Strong Rain' if x >= 6.5 else 'No/Light Rain'
)

final_df = final_df.dropna(subset=['평균기온(℃)'])

print(final_df.head())
print()
final_df.info()
print()

# 시각화 영역

# 조건별 데이터 분류
final_df['day_of_week'] = final_df['date'].dt.dayofweek
final_df['is_weekend'] = final_df['day_of_week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
final_df['temp_bin'] = (final_df['평균기온(℃)'] // 5) * 5

# 평일 출퇴근 vs 주말 피크 vs 기타
def categorize_segment(row):
    if row['is_weekend'] == 'Weekday' and row['hour'] in [8, 9, 18, 19]:
        return 'Weekday Commute'
    elif row['is_weekend'] == 'Weekend' and row['hour'] in [14, 15, 16, 17]:
        return 'Weekend Peak'
    else:
        return 'Other'

final_df['segment'] = final_df.apply(categorize_segment, axis=1)

# 맑은 날 데이터만 별도 추출
clear_days = final_df[final_df['is_rainy'] == 'No/Light Rain']

# 터미널 데이터 출력
print("="*60)
print("시각화 전 주요 지표 확인")
print("="*60)

# 평일/주말 시간대별 대여 패턴 상세
print("[1. 시간대별 이용 패턴 상세 수치]")
hourly_detail = final_df.pivot_table(
    index='hour', 
    columns=['is_weekend', 'is_rainy'], 
    values='rent_count', 
    aggfunc='mean'
)
cols_order = [('Weekday', 'No/Light Rain'), ('Weekday', 'Strong Rain'), 
              ('Weekend', 'No/Light Rain'), ('Weekend', 'Strong Rain')]
hourly_detail = hourly_detail.reindex(columns=[c for c in cols_order if c in hourly_detail.columns])
print(hourly_detail.round(0).fillna(0).astype(int))

# 기온 구간별 요약
print("\n[2. 맑은 날 기온 구간별 요약 통계]")
temp_check = clear_days.groupby('temp_bin')['rent_count'].agg(['count', 'mean']).sort_index()
print(temp_check.round(1))

# 기온구간별 강수 민감도 상세
print("\n[3. 기온 및 강수 조건별 요약 통계]")

# 기온구간과 강수여부로만 그룹화하여 평균 계산
temp_rain_summary = final_df.pivot_table(
    index='temp_bin', 
    columns='is_rainy', 
    values='rent_count', 
    aggfunc='mean'
).round(1)

# 강수 여부에 따른 감소율(%) 계산
if 'No/Light Rain' in temp_rain_summary.columns and 'Strong Rain' in temp_rain_summary.columns:
    temp_rain_summary['Drop_Rate(%)'] = (
        (temp_rain_summary['No/Light Rain'] - temp_rain_summary['Strong Rain']) 
        / temp_rain_summary['No/Light Rain'] * 100
    ).round(1)

print(temp_rain_summary.sort_index(ascending=False).fillna('-'))

# 구간별 강수 민감도 상세
print("\n[4. 구간별 강수 민감도 및 감소율]")
segment_summary = final_df.groupby(['segment', 'is_rainy'])['rent_count'].mean().unstack()
segment_summary = segment_summary.reindex(columns=['No/Light Rain', 'Strong Rain'])
segment_summary['Drop_Rate(%)'] = ((segment_summary['No/Light Rain'] - segment_summary['Strong Rain']) / segment_summary['No/Light Rain'] * 100).round(1)
print(segment_summary)

# 실제 강수 발생 일수 확인
print("\n[5. 요일 유형별 실제 강수 발생 일수(Unique Days)]")

daily_weather_type = final_df[['date', 'is_weekend', 'is_rainy']].drop_duplicates()

rainy_days_count = daily_weather_type.groupby(['is_weekend', 'is_rainy']).size().unstack()
rainy_days_count = rainy_days_count.reindex(columns=['No/Light Rain', 'Strong Rain'])

print(rainy_days_count)
print("-" * 60)
print(f"※ 총 분석 기간: {daily_weather_type['date'].nunique()}일")

'''print(f"1. 자전거 대여 기록이 있는 총 일수: {rentals['date'].nunique()}일")
print(f"2. 기상 데이터가 존재하는 총 일수: {weather_daily['date'].nunique()}일")
print(f"3. 두 데이터가 결합된 최종 분석 일수: {final_df['date'].nunique()}일")

missing_days = set(rentals['date'].unique()) - set(final_df['date'].unique())
if missing_days:
    print(f"※ 분석에서 제외된 날짜 예시: {list(missing_days)[:5]}")'''

print()
print("="*60)

# 그래프 생성

# 평일/주말 시간대별 대여 패턴
hourly_comparison = final_df.groupby(['is_weekend', 'is_rainy', 'hour'])['rent_count'].mean().reset_index()

plt.figure(figsize=(16, 8))
for i, day_type in enumerate(['Weekday', 'Weekend'], 1):
    plt.subplot(1, 2, i)
    sns.lineplot(data=hourly_comparison[hourly_comparison['is_weekend'] == day_type], 
                 x='hour', y='rent_count', hue='is_rainy', marker='o', linewidth=2)
    
    title_ko = '평일' if day_type == 'Weekday' else '주말'
    plt.title(f'{title_ko} 시간대별 평균 대여량 (강수 대비)', fontsize=14, pad=15)
    plt.xlabel('시간 (0-23시)')
    plt.ylabel('평균 대여 건수')
    plt.xticks(range(0, 24, 2))
    plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 기온 및 강수 조건별 히트맵
weather_impact = final_df.groupby(['temp_bin', 'is_rainy'])['rent_count'].mean().unstack().fillna(0)
plt.figure(figsize=(16, 8))
sns.heatmap(weather_impact, annot=True, fmt=".0f", cmap='RdYlGn', cbar_kws={'label': '평균 대여량'})
plt.title('기온 구간 및 강수 조건별 평균 대여량 히트맵', fontsize=14, pad=15)
plt.xlabel('강수 상태')
plt.ylabel('평균기온 구간 (5℃ 단위)')
plt.show()

# 맑은 날 기온 변화에 따른 대여량 추이
all_bins = sorted(clear_days['temp_bin'].unique())

temp_trend_df = clear_days.groupby('temp_bin')['rent_count'].mean().reset_index()

plt.figure(figsize=(16, 8))
sns.lineplot(data=temp_trend_df, x='temp_bin', y='rent_count', 
             marker='o', markersize=12, color='royalblue', linewidth=3,
             markeredgecolor='white', markeredgewidth=2)

plt.title('평균기온 구간별 이용량 변화 추이 (맑은 날)', fontsize=15, pad=20)
plt.xlabel('평균기온 구간 (5℃ 단위)', fontsize=12)
plt.ylabel('평균 대여 건수 (건)', fontsize=12)
plt.xticks(all_bins)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.axvspan(15, 20, color='green', alpha=0.1, label='최적 이용 온도')
plt.legend()
plt.show()


# 주요 구간별 강수 민감도 비교 (Bar Plot)
plt.figure(figsize=(16, 8))
sns.barplot(data=final_df, x='segment', y='rent_count', hue='is_rainy', 
            palette='coolwarm', order=['Weekday Commute', 'Weekend Peak', 'Other'])
plt.title('주요 구간별 강수 민감도 비교', fontsize=14, pad=15)
plt.ylabel('평균 대여 건수')
plt.show()

# 요일 유형별 실제 분석 대상 일수 비교
daily_counts = daily_weather_type.groupby(['is_weekend', 'is_rainy']).size().reset_index(name='day_count')

plt.figure(figsize=(16, 8))
sns.barplot(data=daily_counts, x='is_weekend', y='day_count', hue='is_rainy', 
            palette={'No/Light Rain': 'skyblue', 'Strong Rain': 'salmon'})

plt.title('요일 유형 및 강수 조건별 실제 분석 일수 비교', fontsize=14, pad=15)
plt.xlabel('요일 구분')
plt.ylabel('분석 대상 일수 (일)')
plt.grid(axis='y', alpha=0.3)

for p in plt.gca().patches:
    if p.get_height() > 0:
        plt.gca().annotate(f'{int(p.get_height())}일', 
                           (p.get_x() + p.get_width() / 2., p.get_height()), 
                           ha='center', va='center', fontsize=11, color='black', xytext=(0, 7), 
                           textcoords='offset points')

plt.show()