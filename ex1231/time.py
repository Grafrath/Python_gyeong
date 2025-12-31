import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.unicode.ambiguous_as_wide', True)

file_path = './data/stock-data.csv'

df = pd.read_csv(file_path, encoding='UTF-8')
print(df)
print()
df.info()
print()

df['new_Date'] = pd.to_datetime(df['Date'])

print(df.head(3))
df.info()
print()

df = df.drop(columns=['Date'])

print(df.head(3))
df.info()
print()

print('\n-------- pd.DatetimeIndex --------\n')

print(pd.DatetimeIndex(['2022--12--25', '2024/02/09', '1999.5.5']))
print()
print(type(pd.DatetimeIndex(['2022--12--25', '2024/02/09', '1999.5.5'])))
print()
print(pd.DatetimeIndex(['2022--12--25', '2024/02/09', '1999.5.5']).dtype)
print()

print('\n-------- pd.Timestamp --------\n')

print(pd.Timestamp('04-12-2021'))
print()
print(pd.Timestamp('12-02-2021'))
print()
print(pd.Timestamp('2021-05-05'))
print()
# ??? 월,일,년 일,월,년, 년,월,일 셋 다 잘 먹는데??

print('\n-------- pd.to_datetime --------\n')

# print(pd.to_datetime('2024ㅋ 05ㅎ 15ㅂ')) 에러
print(pd.to_datetime('2024ㅋ 05ㅎ 15ㅂ', format='%Yㅋ %mㅎ %dㅂ'))
print(pd.to_datetime('20240515', format='%Y%m%d'))
print()

dates = ['2023-01-01', '2023/02/01', '2023.03.01']
dt_list = pd.to_datetime(dates, format='mixed')
print(dt_list)
print()

pr_day = dt_list.to_period(freq='D')
print(pr_day)
print()

pr_month = dt_list.to_period(freq='M')
print(pr_month)
print()

pr_year = dt_list.to_period(freq='Y')
print(pr_year)
print()

print('\n-------- pd.date_range --------\n')

ts_ms = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='MS',
    tz='Asia/seoul')
print(ts_ms)
print()

# 3개월 간격
ts_3m = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='3MS',
    tz='Asia/seoul')
print(ts_3m)
print()

'''
D - 1일
B - 1영업일
W - 주
H - 시간
T / min - 분
s - 초
M - 월
MS - 월초
Q - 분기(3,6,9,12)
QS - 분기 시작달 첫날
Y - 년
YS - 년초

2D - 2일간격
3H - 3시간
'''

print('\n-------- 테스트 --------\n')

ts = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='7D',
    tz='Asia/seoul')
print(ts)
print()

ts = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='B',
    tz='Asia/seoul')
print(ts)
print()

ts = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='M',
    tz='Asia/seoul')
print(ts)
print()

print('\n-------- period 배열 --------\n')

ts = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='M')
print(ts)
print()

ts = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='h') # 1시간 간격
print(ts)
print()

ts = pd.date_range(
    start='2024-01-01',
    end=None,
    periods=6,
    freq='2d') # 2일  간격
print(ts)
print()

print('\n-------- dt접근자 --------\n')

df['Year'] = df['new_Date'].dt.year
print(df.head(3))
print()

df['Month'] = df['new_Date'].dt.month
print(df.head(3))
print()

df['Day'] = df['new_Date'].dt.day
print(df.head(3))
print()

df['Quarter'] = df['new_Date'].dt.quarter
print(df.head(3))
print()

df['Day_name'] = df['new_Date'].dt.day_name()
print(df.head(3))
print()

df['M_days'] = df['new_Date'].dt.days_in_month 
print(df.head(3))
print()

df['Date_m'] = df['new_Date'].dt.to_period(freq='m')
print(df.head(3))
print()

df_june = df[df['Date_m'] == '2018-06']
print(df_june)
print()

print('\n-------- 문자 인덱싱 --------\n')

df = df.set_index('new_Date')
df = df.sort_index()

print(df.loc['2018-06-27'])
print()

print(df.loc['2018-07'])
print()

print(df.loc['2018-06-27':'2018-07-02'])
print()

print('\n-------- 시간 인덱싱 --------\n')
# 시간을 활용한 인덱싱

print(df.loc[pd.Timestamp(2018, 6, 27):pd.Timestamp(2018, 7, 2)])
print()

print('\n-------- Timedelta 객체 --------\n')

print(pd.Timedelta(days=1))
print(pd.Timedelta('1 days'))
print()
print(pd.Timedelta('1 days 13 hours 25 minutes 30 seconds'))
print(pd.Timedelta(days=1, hours=13, minutes=25, seconds= 30))
print()

print(pd.to_timedelta(['1 days', '13 hours']))
print()

a = df.index
print(a)
print()

b = a - pd.Timedelta(days=1)
print(b)
print()

c = a + pd.Timedelta(days=1)
print(c)
print()

ts = df.head(10)
print(ts)
print()

print('\n-------- shift --------\n')

print(ts.shift(1))
print()

print(ts.shift(3, freq='D'))
print()

print(ts.asfreq('5D'))
print()

print('\n-------- rolling --------\n')

print(ts.rolling(window=3).sum(numeric_only=True))
print()

print(ts.rolling(window='3D').sum(numeric_only=True))
print()