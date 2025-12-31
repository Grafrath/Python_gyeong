import pandas as pd
import numpy as np

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.unicode.ambiguous_as_wide', True)

file_path = './data/stock-data.csv'

df = pd.read_csv(file_path, encoding='UTF-8')
dates = ['2025-01-01', '2025-01-02', '2025-01-03', '2025-02-01', '2025-02-02']
sales = [200, 250, 300, 150, 400]
df_str = pd.DataFrame ({ 'sales': sales }, index=dates)

print(df_str[[i.startswith('2025-02') for i in df_str.index]]) 

print('\n-------- 문자열 인덱스 --------\n')

print(df_str)
print()

dates_dt = pd.to_datetime(df_str.index)
df_dt =  pd.DataFrame ({ 'sales': sales }, index=dates_dt)
print(df_dt[df_dt.index.month == 2])
print()

print('\n-------- period 인덱스 --------\n')

dates_pr = dates_dt.to_period('M')
df_pr =  pd.DataFrame ({ 'sales': sales }, index=dates_pr)
print(df_pr)
print()
print(df_pr.loc['2025-02'])
print()

print('\n-------- ---------------- --------\n')

# 예제 데이터 생성 (2025년 1월 1일부터 2025년 3월 31일까지)
dates = pd.date_range('2025-01-01', '2025-03-31', freq='D')
sales = np.random.randint(100, 500, size=len(dates))

# DatetimeIndex 사용해서 데이터프레임 생성
df_datetime = pd.DataFrame({'sales': sales}, index=dates)

print(df_datetime)
df_datetime.info()
print()