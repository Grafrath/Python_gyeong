import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_excel('./data/주가데이터.xlsx')

df.info()
print()

df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head(3))
print()

print('\n-------- expand 옵션 --------\n')

df_expand = df['연월일'].str.split('-', expand=True)
print(df_expand.head(3))
print()

df['연월일'] = pd.to_datetime(df['연월일'])
df.info()
print()

df['연'] = df['연월일'].dt.year
df['월'] = df['연월일'].dt.month
df['일'] = df['연월일'].dt.day
df['요일'] = df['연월일'].dt.day_name(locale='korean')

print(df.head(3))
print()