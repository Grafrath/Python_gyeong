import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = sns.load_dataset('titanic')

print('\n======== 누락 데이터 표현 ========\n')

ser1 = pd.Series([1, 2, None])
print(ser1)
print()

ser2 = pd.Series([1, 2, None], dtype='Int64')
print(ser2)
print()

print('\n======== 누락 데이터 제거 ========\n')

# 널값이 하나라도 있는행 제거
df_dropna1 = df.dropna() # axis=0 디폴트
df_dropna1.info()
print()

# 널값이 있는 열 제거
df_dropna1 = df.dropna(axis=1)
df_dropna1.info()
print()

df_age = df.dropna(subset=['age'], axis=0)
df_age.info()
print()

# age, deck중 하나라도 널이면 드랍
df_age_deck = df.dropna(subset=['age', 'deck'], axis=0)
df_age_deck.info()
print()

# 둘다 널이면 드랍
df_age_deck = df.dropna(subset=['age', 'deck'], axis=0, how='all')
df_age_deck.info()
print()

print('\n======== age 널값을 평균값으로 채우기 ========\n')

mean_age = df['age'].mean()
print(mean_age)
print()
df['age'] = df['age'].fillna(mean_age)
print(df['age'])
print()

print('\n======== embark_town(최빈값으로 대체) ========\n')

print(df.describe())
print()

# 문자형 통계정보
print(df.describe(include='object'))
print()

# 고윳값별 카운트
em_freq = df['embark_town'].value_counts(dropna=True)
print(em_freq)
print()

most_freq1 = df['embark_town'].mode()
print('최빈값은: ', most_freq1)
print()

# 최빈값을 시리즈로 반환
most_freq2 = df['embark_town'].mode()[0]
print('최빈값은: ', most_freq2)
print()

# 825~830행 조회
df_et = df['embark_town'][825:831]
print(df_et)
print()

df_et1 = df['embark_town'].iloc[825:831]
print(df_et1)
print()

df_et2 = df.loc[825:830, 'embark_town']
print(df_et2)
print()

df_et3 = df.iloc[825:831]['embark_town']
print(df_et3)
print()

print('\n======== 근사값으로 대체 ========\n')

df2 = df.copy()
df3 = df.copy()
print(df2['embark_town'][825:831])
print()

# 이전행(828)으로 채우기
df2['embark_town'] = df2['embark_town'].ffill()
print(df2['embark_town'][825:831])
print()

# 이후행(830)으로 채우기
df3['embark_town'] = df3['embark_town'].bfill()
print(df3['embark_town'][825:831])
print()

