import pandas as pd
import os

print(os.listdir('./data'))
file_path = r'.\data\read_csv_sample.csv'
print(file_path)
print()

file_path2 = os.path.join('data','read_csv_sample.csv')
print(file_path2)
print()

cur_dir = os.getcwd()
print(cur_dir)
print()

file_path3 = os.path.join(cur_dir, 'data', 'read_csv_sample.csv')
print(file_path3)
print()

file_path4 = r'C:\Users\admin\Desktop\New\Python_gyeong\data\read_csv_sample.csv'
print(file_path4)
print()

file_path5 = r'data\read_csv_sample.csv'
print(file_path5)
print()

print('\n-------- CSV 파일 불러오기 --------\n')
df = pd.read_csv(file_path)
print(df)
print()

df = pd.read_csv(file_path2)
print(df)
print()

df = pd.read_csv(file_path3)
print(df)
print()

df = pd.read_csv(file_path4)
print(df)
print()

df = pd.read_csv(file_path5)
print(df)
print()